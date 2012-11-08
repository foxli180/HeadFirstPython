from string import Template
#Template 模块的相关内容,简单的字符串替换模板

def start_response(resp='text/html'):
     return ('Content-type: '+ resp +'\n\n')
#一个可选的字符串作为参数,用它来创建cgi 的 content-type: 行,缺省为 text/html

def include_header(the_title):
     with open('templates/header.html') as headf:
          head_text = headf.read()
     header = Template(head_text)
     return (header.substitute(title=the_title))
#将从header.html中读入的文件,替换所提供的标题

def include_footer(the_links):
     with open('templates/footer.html') as footf:
          foot_text = footf.read()
     link_string = ''
     for key in the_links:
          link_string += '<a href="'+the_links[key]+'">'+key+'</a>&nbsp;&nbsp;&nbsp;&nbsp;'
     footer = Template(foot_text)
     return(footer.substitute(links=link_string))
#使用一个字符串作为参数,来创建一个 html 页面的尾部,页面本身存于 footer.html 中,
#参数用于动态创建一组动态 html 链接标记,从使用来看,参数应该是一个字典

def start_form(the_url,form_type='POST'):
     return('<form action="'+the_url+'" method="'+form_type+'">')
#返回表单最前面的HTML, 允许调用者制定URL,(表单数据将发送到这个URL)
#还可以指定所要使用的方法


def end_form(submit_msg="Submit"):
     return('<p></p><input type=submit value="'+submit_msg+'"></form>')
#返回表单末尾的html标记,同事允许定制submit按钮的文本

def radio_button(rb_name,rb_value):
     return('<input type="radio" name="'+rb_name+
            '" value="'+rb_value+'">'+ rb_value+'<br/>')
#给定一个单选按钮的名和值,创建一个html 单选按钮,两个参数都是必须的

def u_list(items):
     u_string = '<ul>'
     for item in items:
          u_string += '<li>' +item +'</li>'
     u_string += '</ul>'
     return(u_string)
# 给定一个项列表,将其转化为一个html 列表,每次迭代会像ul增加一个li元素

def header(header_text,header_level=2):
     return ('<h'+str(header_level)+'>'+header_text+
             '</h'+str(header_level)+'>')
#返回一个 html 标题标记,默认为2级标题

def para(para_text):
     return('<p>'+para_text+'</p>')
#段落标记一个文本段



def create_inputs(inputs_list):
     html_inputs = ''
     for each_input in inputs_list:
          html_inputs = html_inputs + '<input type ="Text" name="'+\
                       each_input + '" size=40>'
          return (html_inputs)

def do_form(name, the_inputs,method='POST',text='Submit'):
     with open ('templates/form.html') as formf:
          form_text=formf.read()
     inputs = create_inputs(the_inputs)
     form = Template(form_text)

     return(form.substitute(cgi_name=name,http_method = method,list_of_inputs=inputs,submit_text=text))

     


          
 

