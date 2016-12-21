# learning-journal-basic
Build an online learning journal using Python!

Mockups have been prepared using jinja2 for the following pages:

 - *main* - home page that shows a list of journal entries with just the title and date created.
 - *detail* - detail page that shows a single entry. The title, text and created date should be displayed on this page.
 - *new* - HTML form page you will use to create a new entry. The title and text of the entry are inputs of the form, empty at first.
 - *edit* - HTML form page you will use to edit an existing entry. The title and text of the entry are inputs in this form.

*style.css* has been prepared for the styling of each of the 4 pages using bootstrap.

The learning journal is deployed on: https://claires-learning-journal.herokuapp.com/ utilizing Pyramid.

```
platform darwin -- Python 2.7.11, pytest-3.0.5, py-1.4.32, pluggy-0.4.0
rootdir: /Users/clairegatenby/CF/401/learning-journal-basic, inifile: pytest.ini
plugins: cov-2.4.0
collected 4 items 

learning_journal_basic/tests.py ....

---------- coverage: platform darwin, python 2.7.11-final-0 ----------
Name                                             Stmts   Miss  Cover   Missing
------------------------------------------------------------------------------
learning_journal_basic/__init__.py                   8      0   100%
learning_journal_basic/routes.py                     6      0   100%
learning_journal_basic/views.py                     14      4    71%   57-58, 64-65
------------------------------------------------------------------------------
TOTAL                                               28      4    86%


======================================================= 4 passed in 0.64 seconds 
platform darwin -- Python 3.5.2, pytest-3.0.5, py-1.4.32, pluggy-0.4.0
rootdir: /Users/clairegatenby/CF/401/learning-journal-basic, inifile: pytest.ini
plugins: cov-2.4.0
collected 4 items 

learning_journal_basic/tests.py ....

---------- coverage: platform darwin, python 3.5.2-final-0 -----------
Name                                             Stmts   Miss  Cover   Missing
------------------------------------------------------------------------------
learning_journal_basic/__init__.py                   8      0   100%
learning_journal_basic/routes.py                     6      0   100%
learning_journal_basic/views.py                     14      4    71%   57-58, 64-65
------------------------------------------------------------------------------
TOTAL                                               28      4    86%


======================================================= 4 passed in 0.99 seconds
```