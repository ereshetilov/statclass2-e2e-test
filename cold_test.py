from selenium import webdriver

driver = webdriver.Remote(
    command_executor='http://localhost:9999',
    desired_capabilities={
        
        "app": r"C:/0.0.1/Statclass.exe"
    })



driver.quit()