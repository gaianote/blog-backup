## 基本规则

YAML有以下基本规则： 

1. 大小写敏感 
2. 使用缩进表示层级关系 
3. 禁止使用tab缩进，只能使用空格键 
4. 缩进长度没有限制，只要元素对齐就表示这些元素属于一个层级。 
5. 使用#表示注释 
6. 字符串可以不用引号标注


```yaml
name: junxi
age: 18
spouse:
    name: Rui
    age: 18
children:
    - name: Chen You
      age: 3
    - name: Ruo Xi
      age: 2
```

## 注意

1. key与value之间一定要有空格
2. 诸如 local: '[name = "uname"]' 的形式，value一定要用引号扩住，否则会被当成列表