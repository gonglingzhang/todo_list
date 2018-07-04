# todo_list
刚开始接触django，用其开发的一个todo_list，数据库用的是postgresql，本想用django-rest-framework，结果学得不明不白的，就先用django开发了....

#### 功能简介

- 注册和登陆功能
- 增加一个待做事件
- 修改/完成/删除 一个待做事件
- 将自己的待做事件按照日期进行排序显示
- 查看某一天的待做事件


#### 功能展示
##### 注册和登陆功能
注册功能没有太多限制，只要是邮箱的格式都可以注册成功。
![注册](https://github.com/gonglingzhang/todo_list/blob/master/gif/register.gif)

注册完毕之后进行登陆，不然无法访问自己的“todo事件”，登陆完毕之后，右上角会显示自己的用户名，点击自己的用户名可以查看自己的“todo事件”。
![登陆](https://github.com/gonglingzhang/todo_list/blob/master/gif/login.gif)

##### 增加一个待做事件
登陆之后会跳到新增TODO事件的页面，可以在此页面上添加需要做的事情。
![新增TODO](https://github.com/gonglingzhang/todo_list/blob/master/gif/add_todo.gif)

##### 修改/完成/删除一个待做事件
可以点击某一待做事件，对其进行修改，完成和删除。
![修改](https://github.com/gonglingzhang/todo_list/blob/master/gif/amend.gif)
![完成](https://github.com/gonglingzhang/todo_list/blob/master/gif/finish_todo.gif)
![删除](https://github.com/gonglingzhang/todo_list/blob/master/gif/delete_todo.gif)

##### 查看某一天的待做事件
点击某一天的时间，查看全天待做事件。
![查看某一天的待做事件](https://github.com/gonglingzhang/todo_list/blob/master/gif/todo_in_day.gif)

