# Sticky Notes App

## Description

The Sticky Notes app is a Django web application that allows users to create, view, edit, and delete notes. It follows Django’s Model–View–Template (MVT) architecture and demonstrates full CRUD functionality with tests.

---

## Features

* Create, view, update, and delete notes
* Note detail view
* Delete confirmation page
* Responsive layout using Bootstrap
* Automated tests for models, views, and URLs

---

## Tech Stack

* Python
* Django
* SQLite
* HTML, CSS, Bootstrap

---

## App Structure

* **Model:** `StickyNote`
* **Views:** list, detail, create, update, delete
* **Templates:** base, list, detail, form, confirm delete
* **URLs:** REST-style routing using primary keys
* **Tests:** model, view, and URL tests included

---

## How to Run

```bash
python manage.py migrate
python manage.py runserver
```

---

## Documentation

Design and planning documentation is included in the `docs/` folder, along with supporting diagrams.

---

## Status

✔ Application complete
✔ All tests passing
✔ Documentation added

