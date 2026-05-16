豆包：  
可以实现，而且有两种方案：  
**不用写安卓原生代码**（简单） / **写原生 App**（正规）  
  
## 一、最简单方案：用 Termux 自带 URL Scheme（推荐）  
Termux 支持被其他 App 通过链接唤起并执行命令。  
  
### 唤起格式（浏览器/别的App都能用）  
```  
termux://run/你的命令  
```  
比如：  
```  
termux://run/ls  
termux://run/neovim  
termux://run/cd ~/storage/shared && node index.js  
```  
  
你只要做一个安卓 App，里面一个按钮，点击打开这个 URL 就行。  
  
---  
  
## 二、我直接给你一个最小安卓 App 代码（Android Studio）  
用 Kotlin 做一个只有一个按钮的 App，点击打开 Termux 并执行命令。  
  
### 1. 布局 `activity_main.xml`  
```xml  
<?xml version="1.0" encoding="utf-8"?>  
<LinearLayout  
xmlns:android="http://schemas.android.com/apk/res/android"  
android:layout_width="match_parent"  
android:layout_height="match_parent"  
android:gravity="center">  
  
<Button  
android:id="@+id/btn_run"  
android:layout_width="wrap_content"  
android:layout_height="wrap_content"  
android:text="打开Termux执行命令"/>  
  
</LinearLayout>  
```  
  
### 2. 主代码 `MainActivity.kt`  
```kotlin  
import android.content.Intent  
import android.net.Uri  
import androidx.appcompat.app.AppCompatActivity  
import android.os.Bundle  
import android.widget.Button  
  
class MainActivity : AppCompatActivity() {  
override fun onCreate(savedInstanceState: Bundle?) {  
super.onCreate(savedInstanceState)  
setContentView(R.layout.activity_main)  
  
val btn = findViewById<Button>(R.id.btn_run)  
btn.setOnClickListener {  
// 在这里改你要执行的命令  
val cmd = "ls"  
  
val uri = Uri.parse("termux://run/$cmd")  
val intent = Intent(Intent.ACTION_VIEW, uri)  
startActivity(intent)  
}  
}  
}  
```  
  
### 3. 权限（可选）  
在 `AndroidManifest.xml` 加上：  
```xml  
<queries>  
<package android:name="com.termux" />  
</queries>  
```  
  
这样安装后，点按钮就会：  
**打开 Termux → 自动执行你写的命令**  
  
---  
  
## 三、进阶：后台执行（不弹出 Termux 界面）  
需要安装 **Termux:Tasker** 插件，然后用 Intent 调用。  
你要这种我也可以给你完整代码。  
  
---  
  
你告诉我这 2 个信息，我可以**直接给你最终可编译的完整项目**：  
1. 你要点击后执行的**具体命令**  
2. 想要 **显示 Termux 界面** 还是 **后台悄悄执行**？  
  
内容由 AI 生成