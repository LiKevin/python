# -*- coding: utf-8 -*-
__author__ = 'k22li'

"""
# label, button_2
"""
#import Tkinter
#
#top = Tkinter.Tk()
#top.title('www.lizhihui-kevin.com')
#label = Tkinter.Label(top, text = 'Welcome to Kevin\'s wiki page!', bg = 'blue', fg = 'white')
#label.pack()
#def helloButton():
#    print 'welcome to visit Kevin family'
#
#Tkinter.Label(top, text='red', bg='red', width = 26, height = 1).pack()
#Tkinter.Label(top, text='blue', compound = 'top', bg = 'blue', width = 26, height = 1).pack()
#Tkinter.Label(top, text='green',  compound = 'left', bg = 'green', width = 26, height = 1).pack()
#Tkinter.Button(top, text = 'Hello Button', command = helloButton).pack()
#Tkinter.mainloop()

"""
# button_2
"""
#import Tkinter
#
#top = Tkinter.Tk()
#top.title('www.lizhihui-kevin.com')
#label = Tkinter.Label(top, text = 'Welcome to Kevin\'s wiki page!', bg = 'blue', fg = 'white')
#label.pack()
#def printEventInfo(event):
#    print 'event.time = ', event.time
#    print 'event.type = ', event.type
#    print 'event.WidgetId = ', event.widget
#    print 'event.KeySymbol = ', event.keysym
#
#for i in ['normal', 'active', 'disabled']:
#    button = Tkinter.Button(top, text = i, state = i)
#    button.bind('<Enter>', printEventInfo)
#    button.pack()
##button.focus_set()
#top.mainloop()
#

"""
绑定Button与变量,设置button在textvariable中的属性
"""

#import Tkinter
#root = Tkinter.Tk()
#root.title('www.welcome.lizhihui.homepage.com')
#
#def changeText():
#    if button['text'] == 'text':
#        v.set('change')
#        print 'changed'
#    else:
#        v.set('text')
#        print 'text'
#
#label = Tkinter.Label(root, text='Kevin\'s Homepage', bg='blue', fg = 'white')
#label.focus_set()
#label.pack()
#
#
#v = Tkinter.StringVar()
#button = Tkinter.Button(root,textvariable = v, command = changeText)
#v.set('change')
#button.pack()
#root.mainloop()
#
## 将变量v与Button绑定，当v值变化时，Button显示的文本也随之变化


"""
#Tkinter教程之Entry篇
#Entry用来输入单行文本
"""
#import Tkinter
#root = Tkinter.Tk()
#root.title('www.greeting.from.kevin.com')
#
#entry = Tkinter.Entry(root, text = 'pls. input your name here...') #Entry的text属性不可以设置Entry的文本,所以运行以上代码时，实际上并没有文本显示！！！
#entry.pack()
#
#root.mainloop()

"""
在Entry中设定初始值，使用textvariable将变量与Entry绑定
"""
#import Tkinter
#root = Tkinter.Tk()
#root.title('www.WelcomeKevin.com')
#
#strVar = Tkinter.StringVar()
#entry = Tkinter.Entry(root, textvariable = strVar) #当将字符变量strVar与Entry绑定后，然后将变量赋初始值时，entry中的文本便可以显示了
#strVar.set('Your name here...') #Fixme：须注意此处entry的长度不会随初始字符串的长度变化而调整的
##entry['state'] = 'disabled' #entry的属性亦可被设置为只读的模式，此时不允许终端用户输入任何东西，其他可用状态值：normal，active， disabled
#entry.pack()
#root.mainloop()


"""
Entry: 设置为密码输入框
#将Entry作为一个密码输入框来使用，即不显示用户输入的内容值，用特定符号代替。使用用属性show来指定。
"""
#import Tkinter
#root = Tkinter.Tk()
#root.title('www.KevinHomePage.com')
#
#strVar1 = Tkinter.StringVar()
#entry1 = Tkinter.Entry(root, textvariable = strVar1, show = '*')
#strVar1.set('Write down your name...')
#entry1.pack()
##entry1['show'] = '*'
#
#for mask in ['*', '$', '#']:
#    strVar2 = Tkinter.StringVar()
#    entry2 = Tkinter.Entry(root, textvariable = strVar2)
#    strVar2.set('Password') #Fixme：问题在于初始值一同被置为mask符号，而不能带给用户真正的提示作用，这是用户所不希望看到的
#    entry2.pack()
#    entry2['show'] = mask #attention: mask 符号的长度与初始值相同
#
#root.mainloop()


"""
Entry: 5.验证输入的内容是否符合要求。
使用validate来校验输入的内容
使用validate方法来限制输入的内容
这是一个有问题的例子，无法调用validateText回调函数
"""

#import Tkinter
#root = Tkinter.Tk()
#root.title('www.welcome.com')
#
#strVar = Tkinter.StringVar()
#
#def validateText(textContent):
#    print textContent
#    return textContent.isalnum()
#
#entry = Tkinter.Entry(root, validate = 'key', textvariable = strVar, validatecommand = validateText)
#strVar.set('Validating...') #Fixme: 文档中说明使用validate来接受的事件，使用validatecommand来确定输入的内容是否合法，但如何传入参数？没找到相应的说明
##因此以上测试并没有真正的响应validate事件
#entry.pack()
#
#root.mainloop()


"""
#Tkinter教程之Checkbutton篇
#Checkbutton又称为多选按钮，可以表示两种状态：On和Off，可以设置回调函数，每当点击此按钮时回调函数被调用
"""

#import Tkinter
#
#root = Tkinter.Tk()
#root.title('www.welcome.com')
#
#checkbutton = Tkinter.Checkbutton(root,text = 'CheckButton') #Fixme: 同上，此中只实现了checkbutton gui，但后台响应如何传递暂时没有实现; 方案如下例
#checkbutton.pack()
#root.mainloop()

"""
CheckButton: 设置checkbutton 的回调函数
"""
#import Tkinter
#
#root = Tkinter.Tk()
#root.title('www.welcome.com')
#
#def callback():
#    print 'you checked this button'
#checkbutton = Tkinter.Checkbutton(root, text = 'checkbutton: callbacktest', command = callback)
#checkbutton.pack()
#root.mainloop()

"""
CheckButton: 3.通过回调函数改变Checkbutton的显示文本text的值
"""
#import Tkinter
#
#root = Tkinter.Tk()
#root.title('www.welcome.com')
#
#def changeButtonCallback():
#    print 'here your default value has been changed!'
#    strVal.set('Option enabled')
#
#strVal = Tkinter.StringVar()
#checkbutton = Tkinter.Checkbutton(root, text = 'Default option', textvariable = strVal, command = changeButtonCallback) #注意此处的text = 'Default option'并不起作用，而是strvar杯作为默认的显示
#strVal.set('Option available')
#checkbutton.pack()
#
#root.mainloop()

"""
4.上述的textvariable使用方法与Button的用法完全相同，
使用此例是为了区别Checkbutton的另外的一个属性variable,
此属性与textvariable不同，它是与这个控件本身绑定，Checkbutton自己有值：On和Off值，缺省状态On为1，Off为0，
"""
#import Tkinter

#root = Tkinter.Tk()
#root.title('Test variable attribute!')
#
#v = Tkinter.IntVar()
#
#def callCheckButton():
#    print v.get()
#
#checkButton = Tkinter.Checkbutton(root, variable = v, text = 'checkbutton value', command = callCheckButton) #command = 当checkbox被选中时的函数调用；　variable: checkbox 被选中与否的状态。
#checkButton.pack()
#
#root.mainloop()

"""
5.Checkbutton的值不仅仅是1或0，可以是其他类型的数值，
可以通过onvalue和offvalue属性设置Checkbutton的状态值，
如下代码将On设置为'python',Off值设置为'Tkinter'，
程序的打印值将不再是0或1，而是'Tkinter’或‘python’'''
"""
#import Tkinter
#root= Tkinter.Tk()
#root.title('change the variable default values!')
#v = Tkinter.StringVar()
#
#def callCheckButton():
#    print v.get()
#
#checkButton = Tkinter.Checkbutton(root, variable = v, text = 'update checkbutton value', \
#    command = callCheckButton, onvalue = 'checkbutton On', offvalue = 'checkbutton off')
#checkButton.pack()
#
#root.mainloop()

"""
#Tkinter教程之Radiobutton篇
#Radiobutton为单选按钮，即在同一组内只能有一个按钮被选中，每当选中组内的一个按钮时，其它的按钮自动改为非选中态，与其他控件不同的是：它有组的概念
"""
#fixme:  即在同一组内只能有一个按钮被选中,每当选中组内的一个按钮时，其它的按钮自动改为非选中态

#import Tkinter
#
#root = Tkinter.Tk()
#root.title('RadioButton Basic')
#
#v = Tkinter.IntVar()
#def callbackRadio():
##    print v.get()
#    print 'callback command is executed!'
##for i in range(10):
##    bname = 'radio button' + str(i)
##    bname = Tkinter.Radiobutton(root, variable = v, text = 'radio button %s' %str(i), command = callbackRadio)
##    bname.pack()
#
#rb_1 = Tkinter.Radiobutton(root, text = 'radio button 1', command = callbackRadio)
#rb_1.pack()
#rb_2 = Tkinter.Radiobutton(root, text = 'radio button 2', command = callbackRadio)
#rb_2.pack()
#rb_3 = Tkinter.Radiobutton(root, text = 'radio button 3', command = callbackRadio)
#rb_3.pack()
#
#root.mainloop()
## #不指定绑定变量，每个Radiobutton自成一组

"""
2.创建一个Radiobutton组，使用绑定变量来设置选中哦的按钮
"""

#import Tkinter
#
#root = Tkinter.Tk()
#root.title('bind setting of the selected buttons!')
#
#v = Tkinter.IntVar()
#k = Tkinter.IntVar()
#v.set(1)
#k.set(2)
#
#for i in range(3):
    #    radioButton = Tkinter.Radiobutton(root, variable = v, text = 'Binding Test %s'%str(i), value = i)
    #    radioButton.pack() #variable 参数用来分组ｒａｄｉｏ　ｂｕｔｔｏｎ
    #
    #for i in range(3, 6):
    #    radioButton = Tkinter.Radiobutton(root, variable = k, text = 'Binding Test %s'%str(i), value = i)
    #    radioButton.pack()#注意同一组中的ｖａｌｕｅ值不能相同，否则这两个按钮的工作方式完全相同；即会同时被选中/或同时被ｄｉｓａｂｌｅ
    #
#root.mainloop()

"""
6.Radiobutton另一个比较实用的属性是indicatoron,缺省情况下为1，如果将这个属性改为0，则其外观是Sunken
"""

#import Tkinter
#
#root = Tkinter.Tk()
#root.title('Radio button indicatoron test')
#
#v = Tkinter.IntVar()
#v.set(1)
#
#for i in range(3):
#    radioButton = Tkinter.Radiobutton(root, variable = v, indicatoron = 0, text = 'indicatoron test %s'%str(i), value = i)
#    radioButton.pack()
#
#root.mainloop()



"""
#Tkinter教程之Listbox篇
#Listbox为列表框控件，它可以包含一个或多个文本项(text item)，可以设置为单选或多选
#"""
#
#import Tkinter
#root = Tkinter.Tk()
#root.title('listbox basic settings')
#
#label = Tkinter.Label(root, text = 'Sex selection', bg = 'blue', fg = 'white')
#label.pack()
#
#lb = Tkinter.Listbox(root)
#for item in ['male', 'female']:
#    lb.insert(Tkinter.END, item)
#lb.pack()
#root.mainloop()

"""
2.创建一个可以多选的Listbox,使用属性selectmode
"""

#import Tkinter
#
#root = Tkinter.Tk()
#root.title('Multi-Selectable Listbox')
#
#label = Tkinter.Label(root, text = 'Your Favorite Food:', bg = 'blue', fg = 'white')
#label.pack()
#
##mlb = Tkinter.Listbox(root, selectmode = Tkinter.MULTIPLE)
#mlb = Tkinter.Listbox(root, selectmode = Tkinter.EXTENDED)
#
##mlb = Tkinter.Listbox(root, selectmode = Tkinter.BROWSE) #使用鼠标进行拖动，可以看到选中的位置随之变化。随着鼠标拖动，所选中的ｉｔｅｍ也发生变化
#
#for favorite in ['tomato', 'potato', 'top rice', 'cucumber', 'fish']:
#    mlb.insert(Tkinter.END, favorite)
#mlb.insert(0, 'pork', 'beef', 'mutton') #index '0' means to insert at the first beginning of the lists; while Tkinter.active means insert at the head of the \
##current active item
##mlb.selection_anchor(3)
#mlb.select_set(1,4) # 用来设置默认选中项，　即时没有对ｌｉｓｔｂｏｘ的ｓｅｌｅｃｔｍｏｄｅ属性作任何设置，此代码并未指定Listbox为MULTIPLE或EXTENDED，查通过selection_set仍旧可以对Listbox
##mlb.select_clear(index) # 对应于ｓｅｌｅｃｔ——ｓｅｔ，用来取消选定。
#
#mlb.pack()
#root.mainloop()
## 依次点击这三个item，均显示为选中状态。
## 属性MULTIPLE允许多选，每次点击item，它将改变自己的当前选状态，与Checkbox有点相似


"""
8.得到当前Listbox中的item个数
"""
#
#import Tkinter
#
#root = Tkinter.Tk()
#root.title('Count list items')
#
#mlb = Tkinter.Listbox(root, selectmode = Tkinter.EXTENDED)
#
#for favorite in ['tomato', 'potato', 'top rice', 'cucumber', 'fish']:
#    mlb.insert(Tkinter.END, favorite)
#
#mlb.select_set(2)
#mlb.delete(3,4) #remove the default items from the first index till the defined index
#print mlb.curselection() #ruturn the tuple items, where the index of the selected items are listed one by one
#print mlb.get(1,2) #get the item according to the index, return the tuple formatted results
#
#print mlb.size() #得到当前Listbox中的item个数
#mlb.pack()
#root.mainloop()
#
##例如：返回值为('3', '4', '5', '6', '7', '8')，而不是('300','400','500','600','700','800')，哑然无法直接得到各项的值，知道了索引，得到值
##就很容易了:lb.get()就可以实现。


"""
11.判断 一个项是否被选中，使用索引。 selection_includes
"""
#import Tkinter
#
#root = Tkinter.Tk()
#root.title('Selection Includes Test')
#
#mlb = Tkinter.Listbox(root, selectmode = Tkinter.EXTENDED)
#for favorite in ['tomato', 'potato', 'top rice', 'cucumber', 'fish']:
#    mlb.insert(Tkinter.END, favorite)
#
#mlb.select_set(2, 3) #set the default selected items
#print mlb.curselection()
#print mlb.select_includes(3) #返回结果：True Flase (1/0)，即8包含在选中的索引中，0不包含在选中的索引中
#
#mlb.pack()
#root.mainloop()

"""
12.listbox 它不支持command属性来设置回调函数了，使用bind来指定回调函数,打印当前选中的值
"""
#import Tkinter
#root = Tkinter.Tk()
#root.title('Callback from Listbox')
#
#def callbackListBox(event): #fixme:  for warning purpose: notice this 'event' item as the default param is really needed
#    print 'The current selected item is: %s'%mlb.get(mlb.curselection())
#
#v = Tkinter.StringVar()
#mlb = Tkinter.Listbox(root, listvariable = v)
#
#for i in range(10):
#    mlb.insert(Tkinter.END, str(i*100))
#
#mlb.select_set(2, 6)
#mlb.bind('<Double-Button-1>', callbackListBox) #double click event is binded to this callback functions
#mlb.pack()
#root.mainloop()

"""
Tkinter教程之Scale篇
#Scale为输出限定范围的数字区间，可以为之指定最大值，最小值及步距值
1.创建一个Scale'''
"""
import Tkinter
root = Tkinter.Tk()
root.title('Scale creation')

#scale = Tkinter.Scale(root) ##创建一个垂直Scale，最大值为100，最小值为0，步距值为1。这个参数设置也就是Scale的缺省设置了。
v = Tkinter.StringVar()
scale = Tkinter.Scale(root, \
    from_ = -500, \
    to = 500, \
    resolution = 10, \
    orient = Tkinter.HORIZONTAL,
    variable = v
    ) #生成水平方向的ｓｃａｌｅ
scale.pack()
print v.get() #only get the default value '0' in this way; else it should be created in the callback functions
root.mainloop()