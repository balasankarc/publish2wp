publish2wp - CLI tool to publish posts to wordpress sites

### Installation
 1. clone the repo - `git clone https://gitlab.com/balasankarc/publish2wp.git && cd publish2wp`
 2. `sudo python setup.py install`

### Usage (as executable)
`p2wp [options] <input file> <status>`

##### Options
These options override global environment variable settings

 * -h, --help           --- show the help message and exit
 * --site SITE          --- specify the website URL
 * --username USERNAME  --- specify the username
 * --password PASSWORD  --- specify the password

##### Status
The status of a post can be either 'draft' or 'publish'. The former saves the post as draft and latter publishes the post.

### Setting Credentials
Credentials may be set using three environment variables - 
 * publish2wpsite - Set the site url
 * publish2wpusername - Set the username
 * publish2wppassword - Set the password
 
Warning : Don't store your password in environment variables. It is a security threat.

### Input File syntax
Input file to the program should follow specific syntax. The program uses the following syntax  
> option1:value1  
> option2:value2  
> option3:value3,value4  
> .  
> .  
> .  

Following tags may contain different options listed [below](#options)  

#### Sample file
> title:Sample Post Title  
> content:This is a sample content
> This also is part of content
> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras egestas sem sit amet eleifend semper. Aenean tincidunt viverra enim vel eleifend. Pellentesque sed imperdiet lacus. Maecenas gravida erat nec nunc finibus, sit amet pretium eros porta. Mauris ipsum risus, porta non vehicula id, vehicula a metus. Donec venenatis porttitor orci, at lobortis enim. Curabitur massa diam, tincidunt eu mauris vitae, aliquet congue urna. Vestibulum maximus condimentum scelerisque. Aenean lacinia euismod dui eu tristique. Curabitur tincidunt congue sapien, venenatis pulvinar sapien sodales ac. Mauris vulputate maximus nunc nec tristique. Nam sit amet elementum augue. Aliquam erat volutpat.  
> tags: this,is,a,simple,tag  
> categories: this,is,a,simple,category  

This post will be rendered as shown [here](linktoscreenshot)

#### Options
The following options can be given in the input file.
 * title - The post title - Mandatory
 * content - The post content - Mandatory
 * tags - Tags to the post - Comma Seperated - Optional
 * categories - Categories of the post - Comma Seperated - Optional

### Running Tests
publish2wp uses nose to run tests. To run tests, go to the cloned directory and run `nosetests` command.

### License
publish2wp is released under GPLv3+
