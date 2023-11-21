# ESCOM students REST API

## What is this?
---
This API provides access to public data from ESCOM students, such as their semester, gpa, major, and enrolled clubs. The data is available with the consent of the individual.

### Requirements
You can install all the dependencies using the `Requirements.txt` file, with the command

```pip install -r requirements.txt```

### Resources example
* `/students`: Gets a list of all students.
    * Method: GET
    * Paramenters: None
    * Response: Object

* `/students/{student_id}`: Gets the data of a specific student.
    * Method: GET
    * Parameters: `student_id`: The student ID
    * Response: JSON


Created by @porto-o