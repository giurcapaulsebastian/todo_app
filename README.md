# DPF django assessment project "todo app"

This is the starter project for assessing your django skills.  
You need to implement a basic "todo list app".  
When finished, please create a new branch and open a pull request.

## Tasks

## Implement todo app (`todolist.views.TodoListView`)
*Note: Not all items are mandatory, implement as much as you can.*

* Use the existing model `todolist.models.TodoItem` for saving todo list items.
* add a new field on `TodoItem`: `completed_at` (datetime). It should be filled when the item sa marked as completed.
* Implement **Add item form** (simple text input and & +Add button), placed before the items list.
* **List Todo Items** (most recent items first)
* Each item should start with a "checkbox". When clicking it, it should be marked as complete (submit action to backend, the `TodoItem` should me marked as: `is_completed=True` / `completed_at=now()`)
* Each item must end with a "delete" icon/button. When clicking it, the item should be deleted from database.
* Completed items should have "strikethrough" text decoration (you may use `static/css/main.css` to write your own css)
* implement a management command ("todolist_populate") which deletes the completed items (`is_completed=True`) 
* It would be preferable to use a css framework like Bootstrap (add it to `static/css` and include it using `{% static '' %}`), but it's not mandatory.


Notes:
* actions (submit new item / mark as done / delete) can be either implemented with full page/form submit / refresh, or via javascript/ajax. It's up to you.
* you may add any 3rd party library you wish (either it's a python, django, JS or CSS library/framework). Ex, for ajax calls you may add jQuery.
* if you add js/css libraries, place them in `static` directory, instead pof using their CDN. You may add minified versions. 

## Implement RestAPI with CRUD endpoints for `TodoItem` model (optional)

* You may use any library you want, or create your own api views. 
* The code should be placed in `rest_api/` app. The urls are already imported under `/api/` path.
* implement the following endpoints (their paths don't matter)
    * create TodoItem
    * list items
    * update items (allow updating title / is_completed)
    * delete items
* It would be nice to have a couple of Unit tests, checking the functionality of these endpoints.
