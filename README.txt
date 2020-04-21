sampo (not done yet, please be patient. will got many update later)
=====

Getting Started
---------------

1. Change directory into your newly created project.

    cd sampo1

2. Create a Python virtual environment in case you haven't, using venv. Use anything you used to.

    python3 -m venv env

3. Upgrade packaging tools.

    env/bin/pip install --upgrade pip setuptools

    OR

    python setup.py develop (for development only)

4. Install the project in editable mode with its testing requirements. Only use it if you're going to use automatic testing

    env/bin/pip install -e ".[testing]"

5. Initialize and upgrade the database using Alembic.

    - Generate your first revision.

        env/bin/alembic -c development.ini revision --autogenerate -m "init"

    - Upgrade to that revision.

        env/bin/alembic -c development.ini upgrade head

6. Load default data into the database using a script. You can edit the default from 'models' and 'scripts/initialize_db.py'

    env/bin/initialize_sampo1_db development.ini

7. Run your project's tests. Refers to step 4

    env/bin/pytest

8. Run your project.

    env/bin/pserve development.ini
