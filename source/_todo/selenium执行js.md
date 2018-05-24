1、直接写了js之后执行

2、找到元素并向js传递元素

我想介绍的方法是第二种，因为今天用到了

button=br.find_element_by_css_selector("a.appIco.png")
br.execute_script("$(arguments[0]).click()",button)