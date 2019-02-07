# Gigantum Testing

Automation of Gigantum testing with Selenium.

## Usage

See installation before running these commands.

To run ALL tests, using regular Chrome driver.
Note, this may take a while.

```
$ python3 driver.py
```

To run only example tests in headless mode.

```
$ python3 driver.py test_examples --headless
```

To run ALL tests using the Firefox driver
```
$ python3 driver.py --firefox
```

## Installation

Make sure to create a Virtual Environment for this project.

```
$ python3 -m venv testenv
$ source testenv/bin/activate
$ pip3 install -r requirements.txt
```

Now, install the binary browser drivers.

### Getting ChromeDriver (Google Chrome)

Using MacOS 

```bash
brew install chromedriver
```
### Getting geckodriver (Mozilla Firefox)

Using MacOS

```bash
brew install geckodriver
```

### Git Cheat Sheet
To create a new branch, 
```git checkout -b branchname```

To delete a local branch, 
```git branch -D branchname```

