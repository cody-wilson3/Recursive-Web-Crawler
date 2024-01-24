# Recursive Web Crawler User Manual

**Required Additional Installation Steps:**
* User MUST pip install:
  * requests
  * beautifulsoup4

**Difference Between 'Absolute' and 'Relative' URL's:**
* An Abolute URL has enough information by itself to find a resource on a network and contains a Scheme (required) followed by "://" followed by a Hostname (required):
  * Scheme: usually http, https, ftp, telnet, ssh, etc. This indicates how the program is going to communicate with the outside server.
  * Hostname: comes after the "scheme://" and before the next "/" character. The hostname identifies a machine on the internet. May be an IP address or a human-friendly string that connects to an IP address.
* After the Scheme and Hostname there are the optional componenets:
  * *path*, *query parameters*, and/or *fragments*

* Absolute URL examples:
  * https://duckduckgo.com
  * https://gitlab.cs.usu.edu/erik.falor/cs1440-falor-erik-assn5/-/blob/master/instructions/README.md
* Relative URL examples:
  * duckduckgo.com
  * erik.falor/cs1440-falor-erik-assn5/-/blob/master/instructions/README.md


**From the Command Line:**
* Note: At any time when the program is running, user may use ctrl-C to force quit.
* Navigate to the directory where your crawler.py python file is stored using "cd [directoryname]" to open a directory and "ls" to see what is in the current directory.
* Once in ^^^ directory:
  * type "python crawler.py" and then an *absolute* URL. After the absolute URL, the user may put a specified integer as a depth, overriding the default 3.
    * example: running this command will output
* $ python src/crawler.py https://cs.usu.edu 0

```python
$ python src/crawler.py https://cs.usu.edu 0
Crawling from https://cs.usu.edu to a maximum distance of 0 links
https://cs.usu.edu
Visited 1 unique page in 0.2057 seconds
```
**Common Errors of the Program and Incorrect Usages:**
* Relative URL is provided.
* Sometimes when ctrl-C is being used, it might take a couple times to actually quit. Has to do with some implementations of 3rd party modules in the code.
* If a negative number is provided to override the Maximum Depth, it will default to a Maximum Depth of 3.



