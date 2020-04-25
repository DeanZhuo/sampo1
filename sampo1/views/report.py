from sampo1.views import *

# TODO: sample report, annual report


class ReportViewer(object):
    """view report"""

    def __init__(self, request):
        self.request = request
        self.dbh = get_dbhandler()

    @staticmethod
    def sample_report_table(reportlist):
        """HTML table for sample report"""

        rep_table = div()
        rep_table.add(
            fieldset(       # TODO: filter by user only. check if these works
                input_text(name='filter', label='Filter By User:', placeholder='user name'),
                input_select(name='sort', label='',
                             options=[('asc', 'Ascending'), ('des', 'Descending')]),
            ),
            fieldset(
                table()[
                    thead()[
                        th('Code Number'), th('Position'), th('Taken By'), th('Time')
                    ],
                    tbody()[
                        tuple([
                            tr()[
                                td('%s' % samp['label']),
                                td('%s' % samp['position']),
                                td('%s' % samp['user']),
                                td('%s' % samp['time']),
                            ] for samp in reportlist
                        ])
                    ]
                ]
            )
        )
        return rep_table

    @staticmethod
    def annual_report_table(reportlist):
        """HTML table for annual report"""

        number = 0
        rep_table = div()
        rep_table.add(
            fieldset(  # TODO: filter by group, study, location only. check if these works
                input_select(name='filterby', label='Filter By:',
                             options=[('group', 'Group'), ('study', 'Study'), ('location', 'Location')]),
                input_text(name='filter', label=''),
                input_select(name='sortby', label='Sort By:',
                             options=[('group', 'Group'), ('study', 'Study'), ('location', 'Location')]),
                input_select(name='sort', label='',
                             options=[('asc', 'Ascending'), ('des', 'Descending')]),
            ),
            fieldset(
                table()[
                    thead()[
                        th('Group'), th('Study'), th('Location'), th('Subjects'), th('Sample')
                    ],
                    tbody()[
                        tuple([
                            tr()[
                                td('%s' % samp['group']),
                                td('%s' % samp['study']),
                                td('%s' % samp['location']),
                                td('%s' % samp['subject']),
                                td('%s' % samp['sample']),
                            ] for samp in reportlist
                        ])
                    ]
                ]
            )
        )
        return rep_table

    def sample_report(self):
        """show sample report"""

        req = self.request
        dbh = self.dbh
        content = div()

        trans_list = dbh.TakeReturn.sampleReport()
        report_list = list()
        samp = dict()

        for trans in trans_list:
            tSam = dbh.get_sample(sam=trans.sample_id)
            samp['label'] = tSam.label
            samp['position'] = tSam.getPosition()
            tUsr = dbh.get_user(user=trans.user_id)
            samp['user'] = tUsr.fullname()
            samp['time'] = trans.take_date
            report_list.append(samp)

        content.add(self.sample_report_table(report_list))

        return render_to_response("sampo1:templates/generics_page.mako",  # TODO: report template
                           {'html': content,
                            }, request=req
                           )

    def annual_report(self):
        """show annual report"""

        req = self.request
        dbh = self.dbh
        content = div()

        rep_list = dbh.TakeReturn.annualReport(dbh.session(), date.today().year)
        reportlist = list()
        rowdict = dict()

        for rep in rep_list:
            rowdict['group'] = rep['Group.name']
            rowdict['study'] = rep['Study.study_name']
            rowdict['location'] = rep['Location.name']
            rowdict['subject'] = rep['count(subject)']
            rowdict['sample'] = rep['count(sample']
            reportlist.append(rowdict)

        content.add(self.annual_report_table(reportlist))

        return render_to_response("sampo1:templates/generics_page.mako",  # TODO: report template
                           {'html': content,
                            }, request=req
                           )
