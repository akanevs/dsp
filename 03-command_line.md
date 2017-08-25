# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

> > 
pwd: prints current working directory
mkdir: creates a directory
rmdir: deletes directory
touch: creates new empty file with timing info
rm: deletes a file
mv: move or rename a file
ls -a: list files including dot files
cp: copy file
env: print out current environment specifications
cat: stream a file

---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > 
ls: list files in directory
ls -a: same as ls, but also include names that begin with .
ls -l: same as ls, but in long format
ls -lh: same as ls -l, but with unit suffixes
ls -lah: same as ls -lh, but also includes names that start with .
ls -t: same as ls, but sorted by time
ls -Glp: same as ls, but now colorized, long, and with slash after each filename

---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > 
-c 	Displays files by file timestamp.
-d 	Displays only directories.
-m 	Displays the names as a comma-separated list.
-r 	Displays files in reverse order.
-R 	Displays subdirectories as well.

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> >  The xargs utility reads space, tab, newline and end-of-file delimited strings from the standard input and executes utility
     with the strings as arguments.

 

