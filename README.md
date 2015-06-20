publish2wp - CLI tool to publish posts to wordpress sites

### Installation
 1. clone the repo - `git clone https://gitlab.com/balasankarc/publish2wp.git && cd publish2wp`
 2. `sudo python setup.py install`

### Usage
p2wp \<input file>

### Setting Credentials
Credentials may be set using three environment variables - 
 * publish2wpsite - Set the site url
 * publish2wpusername - Set the username
 * publish2wppassword - Set the password
 
Warning : Don't store your password in environment variables. It is a security threat.

### Input File syntax
Input file to the program should follow specific syntax. The program uses the following syntax  
> \#\<tag1>#  
> \<value to tag 1>  
> \#\<tag2>#  
> \<value to tag 2>  
> .  
> .  
> .  

Tag 1 must be POSTTITLE  
Value of Tag 1 must contain the title of the post  
Following tags may contain different options listed [below](#options)  
Last tag must be POSTBODY  
Following lines constitute the body of the post

#### Sample file
> \#POSTTITLE#  
> Sample Post Title  
> \#POSTBODY#  
> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras egestas sem sit amet eleifend semper. Aenean tincidunt viverra enim vel eleifend. Pellentesque sed imperdiet lacus. Maecenas gravida erat nec nunc finibus, sit amet pretium eros porta. Mauris ipsum risus, porta non vehicula id, vehicula a metus. Donec venenatis porttitor orci, at lobortis enim. Curabitur massa diam, tincidunt eu mauris vitae, aliquet congue urna. Vestibulum maximus condimentum scelerisque. Aenean lacinia euismod dui eu tristique. Curabitur tincidunt congue sapien, venenatis pulvinar sapien sodales ac. Mauris vulputate maximus nunc nec tristique. Nam sit amet elementum augue. Aliquam erat volutpat.
> 
> Aenean ornare vulputate tempor. Cras volutpat odio sed ex tristique, quis dignissim tellus ornare. Donec sollicitudin fermentum erat, sit amet semper ante interdum in. Proin ut dolor et purus gravida ultricies. Donec eu enim eu ex tempus sollicitudin a eu turpis. Aenean justo tellus, tristique et fermentum a, fringilla et enim. Etiam non nisl tristique, suscipit massa eget, vehicula erat. Praesent nibh est, lobortis vitae elit sit amet, dignissim ultrices odio. Suspendisse dignissim lectus sed elit tempus, a sagittis sapien posuere. Praesent sagittis est sem, vitae pulvinar ante fringilla tincidunt. In fringilla consectetur ligula, nec hendrerit dui scelerisque eu. Pellentesque vel blandit purus. Aliquam quis nunc sed leo placerat tincidunt. 

This post will be rendered as shown [here](linktoscreenshot)

#### Options
TODO : Add options

### Running Tests
publish2wp uses nose to run tests. To run tests, go to the cloned directory and run `nosetests` command.

### License
publish2wp is released under GPLv3+
