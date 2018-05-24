## selenium的BY方法

```python
from selenium.webdriver.common.by import By

driver.find_element(By.XPATH, '//button[text()="Some text"]')
driver.find_elements(By.ID, 'loginform')
```

## locator文件

```python
from selenium.webdriver.common.by import By

class MainPageLocators(object):
    GO_BUTTON = (By.ID, 'submit')
```

## 在其他文档调用

```python
driver.find_element(MainPageLocators.GO_BUTTON)
```