
### Basic PyCharm tips and tricks
- How to run python in REPL mode
- How to run one line of Python code
- How to run code block that sits on several lines of Python code
- How to run whole .py file
  - From within PyCharm
    - From terminal
    - REPL - line by line.
  - From terminal

### Basic terminal commands (Windows equivalent commands are in brackets)
- pwd (cd)
- cd
- ls (dir)
- mkdir
- touch (type nul > some_file_name.txt)
- python
- cat
- rm
- rm -rf 
- tree


### Our example folder should look like this
```

mkdir hotel_python
cd hotel_python
mkdir garage
mkdir lobby
mkdir restaurant
mkdir spa_center

cd lobby
mkdir first_floor
mkdir second_floor

cd ..
cd restaurant
mkdir fast_food
mkdir mediteranian_restaurant

cd ..
cd spa_center
mkdir spa_adults
mkdir spa_kids

# When we run command 'tree hotel_python' we should get following output:
hotel_python/
├── garage
├── lobby
│   ├── first_floor
│   └── second_floor
├── restaurant
│   ├── fast_food
│   └── mediteranian_restaurant
└── spa_center
    ├── spa_adults
    └── spa_kids


```
