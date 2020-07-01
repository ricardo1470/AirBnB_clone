> # <a href="AirBnB clone"><img src="https://camo.githubusercontent.com/9ebbf60e208b031d4dcf7db6ffc19fe0339d0ff3/68747470733a2f2f692e6962622e636f2f64354e38354e682f68626e622e706e67" align="middle" width="160" height="60"></a> 0x00. AirBnB clone - The console
---
> ## <a href="AirBnB clone"><img src="https://process.filestackapi.com/resize=width:200/https://cdn.filestackcontent.com/4EAxE8NfTNGVsqHFIXVF" align="middle" width="50" height="50"></a> Table of Contents

* [Introduction](#Introduction)
* [Description](#description)
* [Requirements](#requirements)
* [Installation](#installation)
* [Usage](#usage)
* [Extra Information](#Extra-information)
  * [Tasks](#Tasks)
    * [0. README, AUTHORS](#0.-README,-AUTHORS)
    * [2. Unittests](../tests//)
    * [3. BaseModel](./models/base_model.py)
    * [4. Create BaseModel from dictionary](./models/base_model.py)
    * [5. Store first object](./models/base_model.py)
    * [6. Console 0.0.1](./console.py)
    * [7. Console 0.1](./console.py)
    * [8. First User](./models/user.py)
      * [8.1 First User](./models/engine/file_storage.py)
    * [9. More classes!](./models/state.py)
      * [9.1 More classes!](./models/city.py)
      * [9.2 More classes!](./models/amenity.py)
      * [9.3 More classes!](./models/place.py)
      * [9.4 More classes!](./models/review.py)
    * [10. Console 1.0](console.py)
      * [10. Console 1.0](./models/engine/file_storage.py)
* [Example of Use](#example-of-use)
* [Contact](#Contact)
* [License](#license)
---

## <a href="AirBnB clone"><img src="https://process.filestackapi.com/resize=width:200/https://cdn.filestackcontent.com/4EAxE8NfTNGVsqHFIXVF" align="middle" width="50" height="50"></a> Introduction
**`AirBnB clone - The console`** project is a collaboration between **`Antonio Estela`** and **`Ricardo Camayo`**, Full Stack Software Engineering students at **`Holberton School`**, with which we can emulate the operation of **`AirBnB`**, which contains some of its most basic characteristics, such as : `The console` which starts the entire project **`AirBnB clone`**
## <a href="AirBnB clone"><img src="https://process.filestackapi.com/resize=width:200/https://cdn.filestackcontent.com/4EAxE8NfTNGVsqHFIXVF" align="middle" width="50" height="50"></a> Description
the **`AirBnB clone`** project we will emulate the operation of `The console`, which will provide us with the basic functionalities such as: create, search and delete items that are stored in a dictionary which works as a database
## <a href="AirBnB clone"><img src="https://process.filestackapi.com/resize=width:200/https://cdn.filestackcontent.com/4EAxE8NfTNGVsqHFIXVF" align="middle" width="50" height="50"></a> Requirements
**`AirBnB`** is designed to run in the `Ubuntu 14.04 LTS` linux, `python3` (version3.4.3), you must be able to run python scripts, if you cannot run them contact the administrator for the appropriate permissions
## <a href="AirBnB clone"><img src="https://process.filestackapi.com/resize=width:200/https://cdn.filestackcontent.com/4EAxE8NfTNGVsqHFIXVF" align="middle" width="50" height="50"></a> Installation
Clone this repository: `"https://github.com/ricardo1470/AirBnB_clone.git"`
   * Change directories into the repository: `cd AirBnB_clone`
   * Run the `AirBnB:` `./console.py`
     * Available commands:
       * `EOF`: Exit Console
       * `all`: Displays every instances
       * `count`: Counts the instances
       * `create`: create a new instance with specified name
       * `destroy`: Deletes all attributes
       * `help`: Shows the help
       * `quit`: Exit Consoloe
       * `show`: Displays all attributes
## <a href="AirBnB clone"><img src="https://process.filestackapi.com/resize=width:200/https://cdn.filestackcontent.com/4EAxE8NfTNGVsqHFIXVF" align="middle" width="50" height="50"></a> Usage
The **`AirBnB`** is designed to execute commands interactively and non-interactively.

Interactive mode
```bash
$ ./console.py

(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
(hbnb) quit
$
```

Non interactive mode
```bash
$ echo "help" | ./console.py

(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
$
```

> ## <a href="AirBnB clone"><img src="https://process.filestackapi.com/resize=width:200/https://cdn.filestackcontent.com/4EAxE8NfTNGVsqHFIXVF" align="middle" width="50" height="50"></a> Extra Information
### What’s Included?
| File  | Description  |
|---|---|
| 0. README, AUTHORS  | Write a README  |
| 1. Be PEP8 compliant!   | beautiful code that passes the PEP8 checks.  |
| 2. Unittests  | All your files, classes, functions must be tested with unit tests  |
| 3. BaseModel |  class BaseModel that defines all common attributes/methods for other classes  |
| 4. Create BaseModel from dictionary  | Previously we created a method to generate a dictionary representation of an instance (method to_dict()).  |
| 5. Store first object  | Now we can recreate a BaseModel from another one by using a dictionary representation:  |
| 6. Console 0.0.1  | program called console.py that contains the entry point of the command interpreter  |
| 7. Console 0.1  | command interpreter (console.py) to have these commands  |
| 8. First User  | class User that inherits from BaseModel  |
| 9. More classes!  | those classes that inherit from BaseModel  |
| 10. Console 1.0  | Update FileStorage to manage correctly serialization and deserialization of all our new classes: Place, State, City, Amenity and Review  |


> ## <a href="AirBnB clone"><img src="https://process.filestackapi.com/resize=width:200/https://cdn.filestackcontent.com/4EAxE8NfTNGVsqHFIXVF" align="middle" width="50" height="50"></a> Example of Use
run the console

```bash
./console.py
(hbnb)
```
help

```bash
(hbnb)help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)
```
use help

```bash
(hbnb)help create
 Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id.
(hbnb)
```
Creates a new instance of `BaseModel`

```bash
(hbnb)create BaseModel
ba0824d6-f2d8-4494-84f0-b19bc386e38a
(hbnb)
```
Prints all string representation of all instances

```bash
(hbnb)all
["[BaseModel] (ba0824d6-f2d8-4494-84f0-b19bc386e38a) {'id': 'ba0824d6-f2d8-4494-84f0-b19bc386e38a', 'created_at': datetime.datetime(2020, 7, 1, 15, 34, 25, 759544), 'updated_at': datetime.datetime(2020, 7, 1, 15, 34, 25, 759559)}"]
(hbnb)
```

> ## <a href="AirBnB clone"><img src="https://process.filestackapi.com/resize=width:200/https://cdn.filestackcontent.com/4EAxE8NfTNGVsqHFIXVF" align="middle" width="50" height="50"></a> contact 💬

> Ricardo Camayo

| [twitter](https://twitter.com/RICARDO1470) | [linkedin](https://www.linkedin.com/in/ricardo-alfonso-camayo/) | [mail](1466@holbertonschool.com) | [github](https://github.com/ricardo1470/README/blob/master/README.md) |
|---|---|---|---|

> Antonio Estela

| [twitter](https://twitter.com/Antonio__Estela) | [linkedin](https://www.linkedin.com/in/antonio-jos%C3%A9-estela-7b2a64156/) | [mail](1569@holbertonschool.com) | [github](https://github.com/AntonioEstela) |
|---|---|---|---|
---

## <a href="url"><img src="https://process.filestackapi.com/resize=width:200/https://cdn.filestackcontent.com/4EAxE8NfTNGVsqHFIXVF" align="middle" width="50" height="50"></a> License
*<a href="url"><img src="https://camo.githubusercontent.com/9ebbf60e208b031d4dcf7db6ffc19fe0339d0ff3/68747470733a2f2f692e6962622e636f2f64354e38354e682f68626e622e706e67" align="middle" width="160" height="60"></a>`AirBnB clone - The console` is open source and therefore free to download and use without permission.*

<a href="url"><img src="https://www.holbertonschool.com/holberton-logo.png" align="middle" width="100" height="30"></a>

---
