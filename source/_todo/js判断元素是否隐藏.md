jquery中通过  $("#id").is(":hidden"); 判断一个元素是否是隐藏状态，

其最终调用的代码如下：

```javascript
jQuery.expr.filters.hidden = function( elem ) {
// Support: Opera <= 12.12
// Opera reports offsetWidths and offsetHeights less than zero on some elements
return elem.offsetWidth <= 0 && elem.offsetHeight <= 0;
};
```

因此本质上可以通过元素的offsetWidth  和 offsetHeight 同时小于等于0判断元素是否被隐藏

使用场景：父元素可能设置了display:none 需要判断子元素当前是否显示


代码如下：

```JavaScript
function isElementVisible(el) {
        var rect = el.getBoundingClientRect(),
            vWidth = window.innerWidth || document.documentElement.clientWidth,
            vHeight = window.innerHeight || document.documentElement.clientHeight,
            efp = function (p, x, y) {
                var els = document.elementsFromPoint(x, y); // 获取某点的所有元素, 最顶层的元素在最前面
                for (var index = 0; index < els.length; index++) {
                    var style = getComputedStyle(els[index]);
                    // 如果此前的元素是半透明的，并且不是当前元素，则跳过当前元素
                    if (p != els[index] && (style.opacity < 1 || style.display == 'none' || ['collapse', 'hidden'].indexOf(el.style.visibility) == -1)) {
                        continue;
                    } else return els[index];
                }
                return els[0];
            };
        // Return false if it's not in the viewport
        if (rect.right < 0 || rect.bottom < 0
            || rect.left > vWidth || rect.top > vHeight)
            return false;
  
        return (
            el.contains(efp(el, rect.left, rect.top))
            || el.contains(efp(el, rect.right, rect.top))
            || el.contains(efp(el, rect.right, rect.bottom))
            || el.contains(efp(el, rect.left, rect.bottom)))
            || el.contains(efp(el, rect.left + (rect.right - rect.left) / 2, rect.top + (rect.bottom - rect.top) / 2));
    }
 ```

大致思路：

先判断元素是否在视窗区域内（视窗指浏览器窗口，webview的窗口）
在判断元素的四角和中心点是否在最顶层，如果有遮罩则去掉遮罩的影响（遮罩比如是透明或者半透明的元素）