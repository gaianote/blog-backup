js控制div内的滚动条的位置

通过div的scrollTop变动控制垂直滚动条位置。
通过div的scrollLeft变动控制水平滚动条位置。

示例:

```html
//d1是外层div，带滚动条
<div id='d1' style='height:200px;width:100px;overflow:auto;background:blue;'>
   <div style='height:500px;width:500px;background:yellow'>2222</div>
</div>
```

```javascript
document.getElementById('d1').scrollTop=100;//通过scrollTop设置滚动到100位置
document.getElementById('d1').scrollLeft=200;//通过scrollTop设置滚动到200位置
```
