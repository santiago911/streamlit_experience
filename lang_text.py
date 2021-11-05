# 0 for chinese, 1 for english, 2 for russian

# sidebar.selectbox: page selector
sbar_sbox_0 = ("请选择内容","Please Select A Chapter","Выберите главу")
header = ("Streamlit 体验","Streamlit Experience","Опыт по Стримлайт(Streamlit)")
author = ("作者：刘志昱","Author: Viktor Liu","автор: Виктор Лю")

p_names = (("Streamlit介绍","对象渲染","互动组件","布局、控制流和工具","缓存相关"),
           ("WHAT & WHY Streamlit","Render Objects","Interactive Widgets","Layouts, Control Flow & Utilities","Session_state & Cache"),
           ("Что и Эачем Стримлайт","Визуализировать объект","Интерактивные виджеты","Макеты, поток управления и утилиты","Состояние сеанса и кеш"))
# header warning
header_warning = ("""
                  本文档所呈现的内容可能存在谬误。\n
                  本文档不能替代官方文档。\n
                  """,
                  """
                  Some content in this document may be wrong. \n
                  And this document cannot replace the official document. \n
                  """,
                  """
                  Содержимое, представленное в этом документе, может содержать ошибки.\n
                  Этот документ не может заменить официальный документ.\n
                  """)
# texts
p0intro = ("""
    [✨Streamlit](https://docs.streamlit.io/)是一个可以用于快速搭建Web应用的Python库。\n
    Streamlit官方的定位是服务于机器学习和数据科学的Web应用框架。\n
    当然，您也可以将其用于给自己的Python程序快速创建美观的GUI。\n
    Streamlit与Markdown有异曲同工之妙。它让创作者专注于后端业务的实现，而无需为前端设计分心。\n
    
    ---  
    ##### Streamlit的特色\n
    1. API简明易用\n
        API非常友好，结构清晰，事实上一天就能学会。\n
    2. 无需任何前端知识（HTML CSS JS）就可以构建Web应用\n
        (1) 基于tornado框架，封装大量常用组件方法，支持大量数据表、图表等对象的渲染，支持网格化、响应式布局。\n
        (2) 渲染语言为**Markdown**(GFM)；**支持HTML**文本的渲染。所以也能让你将任何HTML或CSS代码嵌入到应用中。
    3. 社区资源丰富，已成为机器学习界所使用的主流框架。\n
        (1) [官方论坛](https://discuss.streamlit.io/) 非常活跃；\n 
        (2) [Awesome Streamlit](https://awesome-streamlit.org/) 提供了丰富的实例和源码；\n
        (3) 去[Github](https://github.com/)逛逛吧；\n
        (4) 微信群名: Streamlit。这个群并不是我创建的，不过里面有一群技术狂魔互相帮助。\n
        
    ---
    ##### 来两个案例感受一下\n
    1. [德甲联赛数据分析](https://share.streamlit.io/tdenzl/bulian/main/BuLiAn.py)\n
    2. [Slayer St Edition](https://share.streamlit.io/santiago911/slayer-st/main/slayer.py)\n
    3. 这个文档也是用Streamlit制作的哦。
    
    ---
    ##### 什么情况适合用Streamlit？\n
    **作个比较**\n
    (1) 前后端都用JS： Vue + Node + someUI \n
    (2) 前端用HTML 后端用Python： Flask、Django 等等 \n
    (3) 前后端都用Python： Streamlit、PyWebIO 等等 \n
    **我为什么选择Streamlit**\n
    (1) 我需要一个GUI解决方案，能在高效率和美观之间找到平衡，并且注重开发速度和实用性；\n
    (2) 我掌握的前端知识较少，并且没有前端设计艺术细胞；\n
    (3) 我不需要实现太复杂的页面结构与功能；\n
    (4) 我没有精力去涉猎学习成本较高的解决方案了（不然我为什么选择Python）…… \n
    如果我不使用Streamlit，那我就得去学习：CSS，JavaScript，Vue，Node，Bootstrap，Flask，TkInter\n
    
    ---
    ##### 本文档基于以下假设\n
    (1) 您熟练掌握Python；\n
    (2) 您了解Numpy、Pandas、各种可视化库；\n
    (3) 强烈建议您掌握Markdown语言的一般知识。使用Markdown语言将大大提升使用Streamlit的体验。
    """,
    """
    [✨Streamlit](https://docs.streamlit.io/) is a Python library for developing web applications quickly and efficiently. \n
    Its official positioning is a web application framework for machine learning and data science.\n
    Of course, you can also use it to create beautiful GUIs quickly for your Python programs. \n
    Similar to Markdown, Streamlit allows developers to focus on the back-end without being distracted by the front-end design.\n
    
    ---  
    ##### Features of Streamlit\n
    1. Concise and easy-to-learn API\n
        The API is very friendly and actually can be learned in one day.\n
    2. No front-end knowledge (HTML CSS JS) required to build a web app.\n
        (1) Based on TORNADO framework，it encapsulates a lot of common-use component methods, supports the rendering of dataframes, charts and other objects, and supports responsive grid layout. \n
        (2) The rendering language is **Markdown** (GFM); and supports **HTML rendering**. So it also allows you to embed any HTML or CSS code into your application.
    3. Rich-resources community and Famous framework used for machine learning. \n\n
        (1) [Official Forum](https://discuss.streamlit.io/) is very active;\n 
        (2) [Awesome Streamlit](https://awesome-streamlit.org/) provides abundant examples and source code;\n
        (3) Go to [Github](https://github.com/) and find more examples；\n
        (4) Chinese WeChat Group: Streamlit : Not created by me, where hundreds of STers communicate and help each other.\n
        
    ---
    ##### Have a taste of two examples\n
    1. [Bundesliga data analysis](https://share.streamlit.io/tdenzl/bulian/main/BuLiAn.py)\n
    2. [Slayer St Edition](https://share.streamlit.io/santiago911/slayer-st/main/slayer.py)\n
    3. This document you are reading is also made with Streamlit.
    
    ---
    ##### What situation fits Streamlit?\n
    **Make a comparison**\n
    (1) Both front and back ends use JS: Vue + Node + someUI \n
    (2) HTML front-end and Python back-end: Flask, Django, etc. \n
    (3) Both front and back ends use Python: Streamlit, PyWebIO, etc. \n
    **Why I Choose Streamlit**\n
    (1) I need a GUI solution that can find a balance between efficiency and beauty, and have advantages in development speed and practicality;\n
    (2) I am lack of front-end knowledge and not good at art design;\n
    (3) I don’t need pages and functions too complicated;\n
    (4) I have no enough time and energy for knowledges costs too much (also why I choose Python)... \n
    If I don’t use Streamlit, then I have to learn: CSS，JavaScript，Vue，Node，Bootstrap，Flask，TkInter\n
    
    ---
    ##### This document is based on the following assumptions\n
    (1) You are proficient in Python;\n
    (2) You know some about Numpy, Pandas, and common visualization libraries;\n
    (3) Strongly recommended that learning MARKDOWN well. Using Markdown will greatly enhance the experience of Streamlit.
    """,
    """
    [✨Streamlit] (https://docs.streamlit.io/) - это библиотека Python для быстрой и эффективной разработки веб-приложений.\n
    Его официальная позиция - это платформа веб-приложений для машинного обучения и анализа данных. \n
    Конечно, вы также можете использовать его для быстрого создания красивых графических интерфейсов для ваших программ Python. \n
    Подобно Markdown, Streamlit позволяет разработчикам сосредоточиться на серверной части, не отвлекаясь на внешний вид.\n
    
    ---
    ##### Особенности Streamlit \n
    1. Краткий и простой в освоении API \n
        API очень дружелюбен и его можно изучить за один день. \n
    2. Для создания веб-приложения не требуются интерфейсные знания (HTML CSS JS). \n
        (1) Основанный на фреймворке TORNADO, он инкапсулирует множество часто используемых методов компонентов, поддерживает рендеринг фреймов данных, диаграмм и других объектов, а также поддерживает адаптивную компоновку сетки. \n
        (2) Язык визуализации - ** Markdown ** (GFM); и поддерживает ** рендеринг HTML **. Таким образом, он также позволяет вам встраивать любой код HTML или CSS в ваше приложение.\n
    3. Сообщество с богатыми ресурсами и известный фреймворк, используемый для машинного обучения. \n
        (1) [Официальный форум] (https://discuss.streamlit.io/) очень активен; \n
        (2) [Awesome Streamlit] (https://awesome-streamlit.org/) предоставляет множество примеров и исходный код; \n
        (3) Перейдите на [Github] (https://github.com/) и найдите больше примеров; \n
        (4) Китайская группа WeChat: Streamlit: создана не мной, где сотни ST-участников общаются и помогают друг другу. \n
        
    ---
    ##### Два примера \n
    1. [Анализ данных Бундеслиги] (https://share.streamlit.io/tdenzl/bulian/main/BuLiAn.py) \n
    2. [Slayer St Edition] (https://share.streamlit.io/santiago911/slayer-st/main/slayer.py) \n
    3. Этот документ, который вы читаете, также создан с помощью Streamlit.
    
    ---
    ##### Какая ситуация подходит Streamlit? \n
    ** Проведите сравнение ** \n
    (1) И передняя, ​​и задняя стороны используют JS: Vue + Node + someUI \n
    (2) Интерфейс HTML и серверная часть Python: Flask, Django и т. Д. \n
    (3) И передняя, ​​и задняя части используют Python: Streamlit, PyWebIO и т. Д. \n
    ** Почему я выбираю Streamlit ** \n
    (1) Мне нужно решение с графическим интерфейсом, которое может найти баланс между эффективностью и красотой и иметь преимущества в скорости разработки и практичности; \n
    (2) Я не разбираюсь в интерфейсах и не разбираюсь в художественном дизайне; \n
    (3) Мне не нужны слишком сложные страницы и функции; \n
    (4) У меня недостаточно времени и сил, чтобы знания слишком дорого обходились (также почему я выбираю Python) ... \n
    Если я не использую Streamlit, мне придется изучить: CSS, JavaScript, Vue, Node, Bootstrap, Flask, TkInter \n
    
    ---
    ##### Этот документ основан на следующих предположениях \n
    (1) Вы хорошо владеете Python; \n
    (2) Вы кое-что знаете о Numpy, Pandas и общих библиотеках визуализации; \n
    (3) Настоятельно рекомендуется хорошо изучить MARKDOWN. Использование Markdown значительно расширит возможности Streamlit.
    """)
p1t0 = ("Streamlit支持对Python对象的渲染，包括变量、文本、数据表、图表、媒体、状态等等。",
        "Streamlit supports rendering of Python objects, such as variables, texts, dataframes, charts, media, status, etc.",
        "Streamlit поддерживает рендеринг объектов Python, таких как переменные, тексты, фреймы данных, диаграммы, мультимедиа, статус и т. Д.")
p1sbox0 = ("请选择你想了解的内容：","Please choose what you want to know about:","Пожалуйста, выберите то, о чем вы хотите знать:")
p1sbox1 = (("魔术方法","显示文本","显示数据表","显示图表","显示媒体","显示状态"),
           ("Magic Command","Display Text","Display Data(frame)","Display Chart","Display Media","Display Status"),
           ("Магическая команда","Показать текст","Отображение данных","Диаграмма дисплея","Медийная реклама","Состояние дисплея"))
p1t1t1 = ("""
        Streamlit 提供了两种非常好用的“魔术方法”：\n
        (1)输入对象或者其变量名来直接渲染对象(下面简称“直接方法”)；\n
        (2)使用通用方法 st.write(*args, **kwargs)。
        """,
        """
        Streamlit provides two useful 'magic commands':\n
        (1) Input its variable name directly to render the object (as "direct method" below);\n
        (2) Use st.write(*args, **kwargs).
        """,
        """
        Streamlit предоставляет две полезные «волшебные команды»: \n
         (1) Введите имя переменной непосредственно для визуализации объекта (как «прямой метод» ниже); \n
         (2) Используйте st.write (* args, ** kwargs).
        """)
p1t1t2 = ("直接方法","Direct Method","Прямой метод")
p1t1t3 = ("""
        如上所示，可以直接在Streamlit程序中写var_demo，Streamlit会渲染它的值。其他的对象也适用（如果能被渲染）。\n
        此方法的缺点是**无法传递参数**；但是，在不需要传递参数的情况下，是极其方便的。\n
        通常来说，我们的应用的大部分内容由Markdown文本、图表等内容组成，推荐使用这种十分实用的方法。\n
        """,
        """
        As shown above, you can write variable 'var_demo' directly, and Streamlit renders its value then. Other objects can also be rendered (if supported by Streamlit). \n
        The problem of this method is **cannot apply parameters**; however, it is extremely convenient when there is no need to pass parameters. \n
        Generally, most part of our application consists of Markdown text, charts and dataframes. So it is really practical and recommended. \n
        """,
        """
        Как показано выше, вы можете напрямую записать переменную var_demo, и Streamlit отобразит ее значение. Также можно визуализировать другие объекты (если поддерживается Streamlit). \n
        Проблема этого метода в том, что **нельзя применить параметры **; однако это чрезвычайно удобно, когда нет необходимости передавать параметры. \n
        Как правило, большая часть нашего приложения состоит из текста Markdown, диаграмм и фреймов данных. Так что это действительно практично и рекомендуется. \n
        """)
p1t1t4 = ("""
        Object参数可以接收多种对象（请参考官方API文档），而可选键值参数unsafe_allow_html只有在渲染HTML或CSS时才能用到(下文会提及)。\n
        我个人并不喜欢这个方法：与前一种“直接方法”相比，不够“直接”；而和下文介绍的常规方法相比，代码可读性又欠佳，并且不能传递参数。\n
        """,
        """
        The parameter Object can accept kinds of objects that Streamlit supported (please refer to the official API documentation), and the opt-kwargs unsafe_allow_html can only be used when rendering HTML or CSS (mentioned later). \n
        Personally I don't prefer this method: Compared with the 'direct method', it is not 'direct' enough; and compared with the common method mentioned later, this method is lack of readablity and cannot pass parameters. \n
        """,
        """
        Параметр Object может принимать типы объектов, которые поддерживает Streamlit (см. Официальную документацию по API), а opt-kwargs unsafe_allow_html можно использовать только при рендеринге HTML или CSS (упоминается позже). \n
        Лично я не предпочитаю этот метод: по сравнению с «прямым методом» он недостаточно «прямой»; и по сравнению с обычным методом, упомянутым ниже, этот метод не читается и не может передавать параметры. \n
        """)
p1t2t1 = ("""
        Streamlit的渲染语言是Markdown（Github风格）。参考[Github Flavor Markdown](https://github.github.com/gfm)。从前文的魔术方法可以看出，所有的GF Markdown都可以直接输入。\n
        Streamlit提供的st.markdown方法，还支持unsafe_allow_html=False参数，如果改为True，还可以渲染HTML。这使得几乎所有的文字效果甚至是组件都可以通过markdown或者html来实现。"\n
        为方便不了解Markdown的用户，Streamlit也提供了一些常用方法来显示标题、注释、代码、LaTeX等等。这些方法都不如markdown方便，所以，如果你熟悉markdown，则无需关注。\n
        """,
        """
        Streamlit renders text with [Github Flavor Markdown](https://github.github.com/gfm). As MAGIC METHOD shown earlier, all GF Markdown can be rendered. \n
        The *st.markdown* method also supports the kwargs *unsafe_allow_html=False*. If it is TRUE, HTML can also be rendered. It makes almost all kinds of text formats and even components able to be rendered by markdown or html. "\n
        For those users not familiar with Markdown, Streamlit also provides some common methods to display titles, caption, code, LaTeX. These methods are not as convenient as markdown, so if you are familiar with markdown, you don't need to pay attention. \n
        """,
        """
        Streamlit отображает текст с помощью [Github Flavor Markdown] (https://github.github.com/gfm). Как было показано ранее в MAGIC METHOD, все GF Markdown могут быть отображены. \n
        Метод * st.markdown * также поддерживает kwargs * unsafe_allow_html = False *. Если это ИСТИНА, HTML также может отображаться. Он позволяет отображать практически все виды текстовых форматов и даже компоненты с помощью markdown или html. "\n
        Для тех пользователей, которые не знакомы с Markdown, Streamlit также предоставляет некоторые общие методы для отображения заголовков, заголовков, кода, LaTeX. Эти методы не так удобны, как уценка, поэтому, если вы знакомы с уценкой, вам не нужно обращать внимание. \n
        """)
p1t2t2 = ("""
        st.markdown是显示文字最常用的方法，也很好理解。\n
        如果想输入markdown文本，由于不需要传递参数，使用前文提及的“直接方法”就可以了，根本不用写st.markdown。\n
        如果想输入HTML或CSS，则使用st.markdown，并将参数改为True。\n
        顺带一提，Streamlit可以正确引用网络CDN上的css和jquery，却不能识别本地的……如果你要用到Bootstrap，LayUI之类的框架，那应该留意一下。\n
        """,
        """
        st.markdown is the most useful method for displaying text, and very easy to understand. \n
        If you want to input markdown text, since you don't need to pass parameters, you can use the "direct method" mentioned earlier, and don't need to write st.markdown. Otherwise if you want to input HTML or CSS, use st.markdown and change the parameter to TRUE. \n
        By the way, Streamlit can correctly quote the css and jquery on the web CDN, but cannot recognize the local ones... If you want to use frameworks such as Bootstrap or LayUI, you should watch out. \n
        """,
        """
        st.markdown - самый удобный и простой для понимания метод отображения текста. \n
        Если вы хотите ввести текст уценки, поскольку вам не нужно передавать параметры, вы можете использовать «прямой метод», упомянутый ранее, и не нужно писать st.markdown. В противном случае, если вы хотите ввести HTML или CSS, используйте st.markdown и измените параметр на TRUE. \n
        Кстати, Streamlit может правильно цитировать css и jquery в веб-CDN, но не может распознать локальные ... Если вы хотите использовать такие фреймворки, как Bootstrap или LayUI, вам следует быть осторожными. \n
        """)
p1t2t3 = ("""
        st.title, st.header, st.subheader分别对应markdown的#1、#2、#3标题。显然，用markdown要方便得多。\n
        与markdown不同的是，它们可以传入一个参数anchor=None（自定义锚点），锚点可用于在长文档页面的定位。\n
        然而这个功能实在是很鸡肋。第一，Streamlit的锚点只支持英文。第二，无论以何种方式创建，所有的标题都会自动添加一个与标题同名的锚点。第三，如果是长文档，我们通常会使用其他组件进行章节分割。\n
        所以，自定义锚点的用处相对来说非常有限，以上三个方法自然也没有独立使用的意义，推荐使用markdown语言。\n
        """,
        """
        st.title, st.header, st.subheader correspond to #1, #2, #3 title of markdown respectively. Obviously it is much more convenient to use markdown. \n
        Unlike markdown, they accept parameter *anchor=None* (custom anchor point), which can be used for positioning on long documents. \n
        However, this function is really tasteless. First, the anchor of Streamlit only supports English. Second, no matter how they are created, all titles will automatically add an anchor point with the same name as the title. Third, if it is a long document, we usually use other components for chapters division. \n
        Therefore, the usefulness of custom anchors is relatively limited. Those three methods have no much meaning for use. It is recommended to use the markdown language. \n
        """,
        """
        st.title, st.header, st.subheader соответствуют заголовкам # 1, # 2, # 3 уценки соответственно. Очевидно, что гораздо удобнее использовать уценку. \n
        В отличие от уценки, они принимают параметр * anchor = None * (настраиваемая точка привязки), который можно использовать для позиционирования в длинных документах. \n
        Однако это действительно безвкусная функция. Во-первых, якорь Streamlit поддерживает только английский язык. Во-вторых, независимо от того, как они созданы, все заголовки автоматически добавят точку привязки с тем же именем, что и заголовок. В-третьих, если это длинный документ, мы обычно используем другие компоненты для разделения на главы. \n
        Таким образом, использование пользовательских якорей относительно ограничено. Эти три метода не имеют особого смысла для использования. Рекомендуется использовать язык разметки. \n
        """)
p1t2t4 = ("注解用来给其他对象（例如图片、视频）添加说明。",
          "Captions are used to describe other objects, such as pictures or videos.",
          "Подписи используются для описания других объектов, например изображений или видео.")
p1t2t5 = ("st.code用于输入代码块。在markdown中，也有输入代码的语法，即\`\`\`[lang] code \`\`\`。在实际使用中，如果代码量较少，用st.code方法更方便。",
          "st.code is used to input code blocks. In markdown, there is also a syntax for code input like \`\`\`[lang] code \`\`\`. In common use, if the code is short, it is more convenient to use st.code.",
          "st.code используется для ввода блоков кода. В markdown есть также синтаксис для ввода кода, например \`\`\`[lang] code \`\`\`. Обычно, если код короткий, удобнее использовать st.code.")
p1t2t6 = ("输入普通文本。有趣的是，st.text和markdown的普通文本格式是不同的。",
          "Input normal text. Funny that st.text and markdown normal text are different.",
          "Введите обычный текст. Забавно, что st.text и нормальный текст уценки разные.")
p1t2t7 = ("输入LaTeX文本。Markdown本身也可以通过$号快速输入LaTeX。从左侧效果看，似乎st.latex更好一些。",
          "Input LaTeX. Markdown also supports LaTeX input by the $ sign. From the effect on the left side, it seems that st.latex is better.",
          "Введите LaTeX. Markdown также поддерживает ввод LaTeX с помощью знака $. По эффекту слева кажется, что латекс лучше.")
p1t3t1 = ("""
        Streamlit提供了st.dataframe和st.table来显示表格。当然，别忘了，Markdown也可以拿来做表格。\n
        两种表格可接收的对象基本相同；显著区别是st.table是静态表格，而st.dataframe支持点击表头排序。就我个人偏好而言，我更喜欢用st.dataframe（如果需要排序）和Markdown（控制内容更灵活）。\n
        Streamlit还提供了可以展示数据变动的小卡片st.metric。st.json可以展示json，有一说一，有点儿丑。\n
        """,
        """
        Streamlit provides *st.dataframe* and *st.table* to display dataframes. Of course don’t forget Markdown can also be used to create a table. \n
        The objects that can be accepted by these two methods are almost the same; the significant difference is that st.table is a static table, while st.dataframe supports sorting by clicking the header. Personally, I prefer to use st.dataframe (if sorting required) and Markdown (more flexible to control contents). \n
        Streamlit also provides a cute card *st.metric* that can display data changes. *st.json* can display json, which honestly is a bit ugly. \n
        """,
        """
        Streamlit предоставляет * st.dataframe * и * st.table * для отображения фреймов данных. Конечно, не забывайте, что Markdown также можно использовать для создания таблицы. \n
        Объекты, которые могут быть приняты этими двумя методами, почти одинаковы; существенная разница в том, что st.table - статическая таблица, а st.dataframe поддерживает сортировку, щелкая заголовок. Лично я предпочитаю использовать st.dataframe (если требуется сортировка) и Markdown (более гибкий для управления содержимым). \n
        Streamlit также предоставляет симпатичную карточку * st.metric *, которая может отображать изменения данных. * st.json * может отображать json, что, честно говоря, немного некрасиво. \n
        """)
p1t3t2 = ("""
        st.dataframe和st.table支持的数据类型有：np.ndarray, pd.DataFrame, pd.Styler（可为数据设置格式）, pyarrow.Table（需修改设置以支持）, Iterable, Dict。\n
        st.dataframe的参数可以设置固定宽、高（像素）；st.table则是自动根据容器宽度调整。\n
        """,
        """
        The data types supported by st.dataframe and st.table are: np.ndarray, pd.DataFrame, pd.Styler (allowing data format settings), pyarrow.Table (settings need to be modified to support), Iterable, Dict. \n
        The st.dataframe can be set to a fixed width and height (int pixels); st.table is automatically adjusted according to the width of its container. \n
        """,
        """
        Типы данных, поддерживаемые st.dataframe и st.table: np.ndarray, pd.DataFrame, pd.Styler (с возможностью настройки формата данных), pyarrow.Table (настройки необходимо изменить для поддержки), Iterable, Dict. \n
        Для st.dataframe можно задать фиксированную ширину и высоту (целые пиксели); st.table автоматически регулируется в соответствии с шириной контейнера. \n
        """)
p1t3t3 = ("""
        st.metric是用来展示数据变化趋势的小卡片。文字会显示为三行，分别对应label(标签)、value(当前值)、delta(变化值)。\n
        label必须为str。value和delta可以是int、float，甚至也可以是str。如果value为None，则会显示为横线；delta为None，则会隐藏。\n
        delta_color为数据变化的配色，默认为normal（绿升红降），还可以设置为inverse（红升绿降）、off（无颜色）。\n
        """,
        """
        st.metric is a tiny cute card used to show the trend of data changes. The text will display in three lines, corresponding to label (label), value (current value), delta (change value). \n
        label must be str. value and delta can be int, float, or even str. If value is None, it will display as a dash line; if delta is None, it will hide. \n
        delta_color is the color of the data change, the default is normal (green up and red down), it can also be set to inverse (red up and green down), off (no colors). \n
        """,
        """
        st.metric - это крошечная симпатичная карточка, которая показывает тенденцию изменения данных. Текст будет отображаться в трех строках, соответствующих метке (метке), значению (текущему значению), дельте (изменению значения). \n
        метка должна быть str. значение и дельта могут быть int, float или даже str. Если значение равно None, оно будет отображаться пунктирной линией; если дельта None, она будет скрыта. \n
        delta_color - это цвет изменения данных, по умолчанию - нормальный (зеленый вверх и красный вниз), он также может быть установлен на инверсный (красный вверх и зеленый вниз), выкл. (без цветов). \n
        """)
p1t3t4 = ("JSON的结构与字典相似。在Streamlit中输出字典，也是这样的格式。",
          "The structure of JSON is similar to dict. Rendering a dict in Streamlit is also the same format.",
          "Структура JSON аналогична dict. Визуализация dict в Streamlit также выполняется в том же формате.")
p1t4t1 = ("""
        Streamlit支持多种主流图表；目前不支持echarts，但是有第三方库[streamlit-echarts](https://github.com/andfanilo/streamlit-echarts)。\n
        Streamlit内置了三个图表：*st.line_chart*,*st.area_chart*,*st.bar_chart*，还提供了一个内置的*st.map*显示地图。这些功能无需第三方依赖；地图功能建议使用[高德](https://lbs.amap.com/)等第三方API。"\n
        """,
        """
        Streamlit supports kinds of charts libraries; echarts is not supported so far, however there is a third-party library [streamlit-echarts](https://github.com/andfanilo/streamlit-echarts). \n
        Streamlit has three built-in charts: *st.line_chart*,*st.area_chart*,*st.bar_chart* and also provides a built-in *st.map* to display map. These functions do not require dependence; for map it is recommended using third-party APIs such as [AMAP](https://lbs.amap.com/). "\n
        """,
        """
        Streamlit поддерживает различные виды библиотек диаграмм; echarts пока не поддерживается, однако существует сторонняя библиотека [streamlit-echarts] (https://github.com/andfanilo/streamlit-echarts). \n
        Streamlit имеет три встроенных диаграммы: * st.line_chart *, * st.area_chart *, * st.bar_chart *, а также предоставляет встроенную * st.map * для отображения карты. Эти функции не требуют зависимости; для карты рекомендуется использовать сторонние API, такие как [AMAP] (https://lbs.amap.com/). "\n
        """)
p1t4t2 = ("这三个图表是Streamlit内置的，参数相同。width和height为宽高的像素值，use_container_width为使用容器宽度，优先级高于width和height。通常不需要设置参数。\n",
          "These three charts are built-in and have the same parameters. Width and height are the pixel values of chart width and height, and use_container_width means using the width of its container, which priority is higher than width and height parameters.For common use no parameters need to be set.\n",
          "Эти три диаграммы являются встроенными и имеют одинаковые параметры. Ширина и высота - это значения ширины и высоты диаграммы в пикселях, а use_container_width означает использование ширины его контейнера, приоритет которого выше, чем у параметров ширины и высоты. Для обычного использования параметры устанавливать не нужно.\n",)
p1t4t3 = ("这个内置方法仅支持根据经纬度在地图上做标记。如果需要专业地图功能，请使用第三方API。要求传入的数据data为经纬度，并且列名必须为lat（纬度latitude）和lon（经度longitude）。zoom参数是地图缩放等级。use_container_width为使用容器宽度。\n",
          "This built-in method only supports marking on the map based on latitude and longitude. If you need professional map service, please use third-party APIs. The parameter data must be latitude and longitude, and its column names must be lat (latitude) and lon (longitude). The *zoom* parameter is the zoom level of the map. *use_container_width* means the use container width.\n",
          "Этот встроенный метод поддерживает только маркировку на карте по широте и долготе. Если вам нужен профессиональный картографический сервис, используйте сторонние API. Данные параметра должны быть широтой и долготой, а имена столбцов должны быть lat (широта) и lon (долгота). Параметр * zoom * - это уровень масштабирования карты. * use_container_width * означает ширину используемого контейнера.\n")
p1t4t4 = ("第三方图表",
          "Third-Party Chart Libraries",
          "Сторонние библиотеки диаграмм")
p1t4t5 = ("Streamlit目前支持的第三方图表库包括matplotlib、altair、vega_lite、plotly、bokeh、pydeck、graphviz。详细API请参考官方文档。因第三方依赖占用资源，本文档不再逐一展示。\n",
          "The third-party chart libraries currently supported by Streamlit include matplotlib, altair, vega_lite, plotly, bokeh, pydeck, graphviz. Please refer to the official documentation for detailed API. Due to third-party libraries occupy resources, examples will not be shown in this document.\n",
          "Сторонние библиотеки диаграмм, которые в настоящее время поддерживаются Streamlit, включают matplotlib, altair, vega_lite, plotly, bokeh, pydeck, graphviz. Пожалуйста, обратитесь к официальной документации для получения подробной информации об API. Поскольку сторонние библиотеки занимают ресурсы, примеры не будут показаны в этом документе.\n")
p1t5t1 = ("显示图像，视频，音频。",
          "Display images, videos and audios.",
          "Отображение изображений, видео и аудио.")
p1t5t2 = ("""
        ###### 参数说明：\n
        st.image可以渲染一个或者一组图片。如果需要同时渲染多个图片，则image参数、caption参数（如果需要）应传入图片对象的列表。下文用类似[str]的形式表示。\n
        (1)image: np.ndarray,[np.ndarray],BytesIO, str or [str]\n
        np.ndarray,[np.ndarray]类型: 通过np.ndarray对象绘制图片。支持单色、彩色或RGBA图像。\n
        BytesIO类型：从内存中读取Bytes绘制图片。支持单色、彩色或RGBA图像。\n
        str, [str]类型：通过本地路径或网络URL读取图片。\n
        (2) caption: str or [str]\n 
        图片的注解。\n
        (3) width: int or None \n
        图片的宽度（像素）。None表示使用图片本身的宽度。如果是SVG图片，必须设置int宽度。\n
        (4) use_column_width:"auto",True,False \n
        是否使用列宽（容器宽度），优先级高于width。True为使用列宽，False为使用图片宽度（无论是否超过列宽）。auto为自适应，即使用图片宽度，但不能超过列宽。\n
        (5) clamp:bool\n 
        仅对字节数组图像有效。将字节范围设置标准化为0-255。\n
        (6) channel:'RGB'(default) or 'BGR'\n
        颜色通道的顺序。仅对字节数组图像有效。一般是RGB，但是OpenCV之类的库要用到BGR。\n
        (7) output_format:'auto','JPEG','PNG'\n
        输出图片的格式。普通图片可以用有损压缩的jpeg，而数据图表应使用无损压缩的png。auto为自动根据对象类型选择。\n
        """,
        """
        ###### Parameter:\n
        st.image can render one or a group of pictures. If a group of images need to be rendered at the same time, the *image* parameter and *caption* parameter (if needed) should be passed in a LIST of image objects. This is expressed like '[str]' below. \n
        (1)image: np.ndarray,[np.ndarray], BytesIO, str or [str]\n
        np.ndarray,[np.ndarray] type: draw picture(s) through np.ndarray object. It supports monochrome, color or RGBA images. \n
        BytesIO type: read Bytes from memory to draw picture(s). It supports monochrome, color or RGBA images. \n
        str, [str] type: read picture(s) from local path or web URL. \n
        (2) caption: str or [str]\n
        Caption of the picture(s). \n
        (3) width: int or None \n
        The width of the picture (pixels). None means to use the width itself. For an SVG image, an int width must be set. \n
        (4) use_column_width:"auto",True,False \n
        Whether to use column width (container width), and the priority is higher than width parameter. True to use the column width, False to use the image width (no matter whether it exceeds the column width). Auto means to adapt, that is, use the image width as default, but use the column width if it exceeds the column width. \n
        (5) clamp:bool\n
        Only valid for byte array images. Standardize the byte color range to 0-255. \n
        (6) channel:'RGB'(default) or'BGR'\n
        The order of the color channels. Only valid for byte array images. Generally it is RGB, but libraries such as OpenCV use BGR. \n
        (7) output_format:'auto','JPEG','PNG'\n
        The format of the output image. Pictures can use lossy compressed jpeg, and charts should use lossless compressed png. auto means automatically selected according to the object type. \n
        """,
        """
        ###### Параметр: \n
        st.image может отображать одно или несколько изображений. Если группа изображений должна быть визуализирована одновременно, параметр * image * и параметр * caption * (при необходимости) должны быть переданы в СПИСКЕ объектов изображения. Это выражается как "[str]" ниже. \n
        (1) изображение: np.ndarray, [np.ndarray], BytesIO, str или [str] \n
        np.ndarray, тип [np.ndarray]: рисовать картинки через объект np.ndarray. Он поддерживает монохромные, цветные или RGBA-изображения. \n
        Тип BytesIO: чтение байтов из памяти для рисования изображений. Он поддерживает монохромные, цветные изображения или изображения RGBA. \n
        str, [str] type: читать изображения с локального пути или веб-адреса. \n
        (2) подпись: str или [str] \n
        Подпись к картинке (ам). \n
        (3) ширина: int или None \n
        Ширина картинки (в пикселях). Нет означает использование самой ширины. Для изображения SVG должна быть установлена ​​ширина int. \n
        (4) use_column_width: "auto", True, False \n
        Следует ли использовать ширину столбца (ширину контейнера), и приоритет выше, чем параметр ширины. True, чтобы использовать ширину столбца, False, чтобы использовать ширину изображения (независимо от того, превышает ли она ширину столбца). Авто означает адаптацию, то есть использовать ширину изображения по умолчанию, но использовать ширину столбца, если она превышает ширину столбца. \n
        (5) зажим: bool \n
        Действительно только для изображений байтовых массивов. Стандартизируйте диапазон цвета байта до 0-255. \n
        (6) канал: 'RGB' (по умолчанию) или 'BGR' \n
        Порядок цветовых каналов. Действительно только для изображений байтовых массивов. Обычно это RGB, но библиотеки, такие как OpenCV, используют BGR. \n
        (7) output_format: 'авто', 'JPEG', 'PNG' \n
        Формат выходного изображения. Изображения могут использовать сжатый jpeg с потерями, а диаграммы должны использовать сжатый без потерь png. auto означает автоматический выбор в соответствии с типом объекта. \n
        """)
p1t5t3 = ("读取本地图片",
          "Read and Display Local Path Images",
          "Чтение и отображение изображений локального пути")
p1t5t4 = ("""
        ###### 参数说明：\n
        (1) data: str, bytes, BytesIO, np.ndarray, or file \n
        str : 音视频的本地路径或网络URL。\n
        bytes, np.ndarray : 音视频的bytes或ndarray对象。\n
        BytesIO : 从内存读取Bytes音视频对象。\n
        file: with open 读取的音视频对象。\n
        (2) format \n
        文件的MIME格式。参考[媒体类型](https://www.iana.org/assignments/media-types/media-types.xhtml)\n
        (3) start_time \n
        音视频开始播放的时间定位。\n
        """,
        """
        ###### Parameters\n
        (1) data: str, bytes, BytesIO, np.ndarray, or file \n
        str: Local path or web URL of the video or audio. \n
        bytes, np.ndarray: bytes or ndarray object of the video or audio. \n
        BytesIO: read Bytes of the video or audio objects from memory. \n
        file: 'with open' object read from the video or audio file. \n
        (2) format \n
        The MIME format of the file. Refer to [Media Types](https://www.iana.org/assignments/media-types/media-types.xhtml)\n
        (3) start_time \n
        Start time positioning of the video or audio. \n
        """,
        """
        ###### Параметры \n
        (1) данные: str, bytes, BytesIO, np.ndarray или файл \n
        str: локальный путь или веб-адрес видео или аудио. \n
        bytes, np.ndarray: байты или объект ndarray видео или аудио. \n
        BytesIO: чтение байтов видео или аудио объектов из памяти. \n
        file: объект "с открытым", прочитанный из видео или аудио файла. \n
        (2) формат \n
        Формат MIME файла. См. [Типы мультимедиа] (https://www.iana.org/assignments/media-types/media-types.xhtml) \n
        (3) start_time \n
        Начало позиционирования видео или аудио по времени. \n
        """)
p1t5t5 = ("音视频渲染示例",
          "Examples: Display videos and audios",
          "Примеры: отображение видео и аудио.")
p1t6t1 = ("Streamlit提供了一些显示状态的组件。",
          "Streamlit provides some components that display status.",
          "Streamlit предоставляет некоторые компоненты, отображающие состояние.")
p1t6t2 = ("这些方法提供信息（蓝色）、成功（绿色）、警告（橙色）、异常和错误（红色）的提示性信息显示。不仅可以用于信息提示，也可以用来高亮文字，非常实用。",
          "These methods provide informative displays of information (blue), success (green), warning (orange), exception and error (red). They can be used for not only information prompts but also text-highlight, which is very practical.",
          "Эти методы обеспечивают информативное отображение информации (синий), успеха (зеленый), предупреждения (оранжевый), исключения и ошибки (красный). Их можно использовать не только для информационных подсказок, но и для выделения текста, что очень удобно.")
p1t6t3 = ("一个小彩蛋。不保证在所有浏览器中都可以呈现。",
          "A cute easter egg. Not guaranteed that it can be rendered in every browser.",
          "Симпатичное пасхальное яйцо. Не гарантируется, что его можно отобразить в любом браузере.")
p1t6t4 = ("""
        st.progress进度条提供动态的进度显示，而st.spinner等待条则是静态的等待提示。你也可以使用其他基于CSS的组件来替代。\n
        等待条支持文本参数，你可以以变量的形式将进度信息添加到文本中。\n
        需要注意的是，使用以上组件以后，在进度结束前，组件以下的内容都处在灰色的不可用状态。（类似Streamlit正在渲染时的状态）\n
        """,
        """
        st.progress provides a dynamic display of a progress bar, while st.spinner is a static waiting status. You can also use other CSS-based components instead. \n
        st.spinner supports text parameter, and you can add progress information to the text in the form of variable(s). \n
        Notice that when using these two components, the content below the components will be grayed out and unavailable until the progress ends. (Similar to the state when Streamlit is rendering)\n
        """,
        """
        st.progress обеспечивает динамическое отображение индикатора выполнения, а st.spinner - статический статус ожидания. Вместо этого вы также можете использовать другие компоненты на основе CSS. \n
        st.spinner поддерживает текстовый параметр, и вы можете добавлять информацию о ходе выполнения в текст в виде переменных. \n
        Обратите внимание, что при использовании этих двух компонентов содержимое под компонентами будет неактивным и недоступным до завершения выполнения. (Аналогично состоянию при рендеринге Streamlit) \n
        """)
p1t7t1 = ("""
        Streamlit提供了大量交互组件。这些组件有如下特性：\n
        (1)每个组件自身都有返回值，因此不需要回调函数（当然如果有需要也可以从参数设置）。\n
        (2)每当组件的状态值发生变化（例如按钮被点击、输入值被修改等等），会触发整个应用的重新运行（rerun）。通常来说很方便，但是对于大型应用、特别是组件存在组合、嵌套时，就需要使用缓存机制（session_state和cache，下文会讲解）。\n
        (3)组件易于理解和使用，有一些公共的含义相同或相似的标准参数，下文会讲解。大部分参数通常无需修改，使用方便。\n
        """,
        """
        Streamlit provides many interactive components, which have these features:\n
        (1) Every component itself has a return value, so callback functions are not required (of course, callbacks can be set by the parameters on_click or on_change if necessary). \n
        (2) Whenever the state or value of a component changes (for example, button clicked or input-value modified, etc.), it will trigger a automatic rerun of the entire application. Usually it is convenient, but for large applications, especially when components are combined or nested, caching mechanisms (session_state and cache, which will be explained below) are needed. \n
        (3) The components are easy to understand and use, and there are some common standard parameters with the same or similar meaning, which will be explained below. Most of the parameters usually do not need to be modified and are easy to use. \n
        """,
        """
        Streamlit предоставляет множество интерактивных компонентов, которые обладают следующими функциями: \n
         (1) Каждый компонент сам по себе имеет возвращаемое значение, поэтому функции обратного вызова не требуются (конечно, обратные вызовы могут быть установлены параметрами on_click или on_change, если необходимо). \n
         (2) Каждый раз, когда состояние или значение компонента изменяется (например, нажатие кнопки или изменение входного значения и т. Д.), Запускается автоматический повторный запуск всего приложения. Обычно это удобно, но для больших приложений, особенно когда компоненты объединены или вложены, необходимы механизмы кэширования (session_state и cache, которые будут объяснены ниже). \n
         (3) Компоненты просты для понимания и использования, и есть некоторые общие стандартные параметры с одинаковым или похожим значением, которые будут объяснены ниже. Большинство параметров обычно не требуют изменения и просты в использовании. \n
         """)
p1t7t2 = ("""
        ###### 公共参数通览
        |参数|类型|说明|适用组件|
        |---|---|---|---|
        |label|str|组件的标签文字|所有|
        |key|str or int|组件在session_state中的唯一键名|所有|
        |help|str|组件的帮助文字|所有|
        |on_click / on_change,*args,**kwargs|函数名|自定义的组件回调函数和参数|所有|
        |value||渲染时的默认值|checkbox,slider,select_slider,text_input,number_input,date_input,time_input,text_area,color_picker|
        |index|int|渲染时的默认选中项的索引|radio,selectbox|
        |options|iterable|组件可选选项|radio,selectbox,multiselect,select_slider|
        |format_func|函数名|选项格式化函数|radio,selectbox,multiselect,select_slider|
        |min_value & max_value|int or float or date|值域|slider,number_input,date_input|
        |max_chars|int|最大字符数|text_input,text_area|
        |step|int or float|步长|slider,number_input|
        |format|%.|值的格式|slider,number_input|
        """,
        """
        ###### Parameters Overview
        |Parameter|Type|Description|Related Components|
        |---|---|---|---|
        |label|str|Label text of a component|All|
        |key|str or int|Unique key name of a component in session_state|All|
        |help|str|Help text of a component|All|
        |on_click / on_change,*args,**kwargs|Function name|Custom callback function and its parameters of a component|All|
        |value||Default value when rendered|checkbox,slider,select_slider,text_input,number_input,date_input,time_input,text_area,color_picker|
        |index|int|Default selected item's index when rendered|radio,selectbox|
        |options|iterable|Component's optional items|radio,selectbox,multiselect,select_slider|
        |format_func|Function name|Options' formatting function|radio,selectbox,multiselect,select_slider|
        |min_value & max_value|int or float or date|Valid value range|slider,number_input,date_input|
        |max_chars|int|Maximum number of characters input|text_input,text_area|
        |step|int or float|Step length|slider,number_input|
        |format|%.|Value format|slider,number_input|
        """,
        """
        ###### Обзор параметров
        | Параметр | Тип | Описание | Связанные компоненты |
        | --- | --- | --- | --- |
        | label | str | Текст метки компонента | Все |
        | key | str или int | Уникальное имя ключа компонента в session_state | Все |
        | help | str | Текст справки компонента | Все |
        | on_click / on_change, * args, ** kwargs | Имя функции | Пользовательская функция обратного вызова и ее параметры компонента | Все |
        | value || Значение по умолчанию при визуализации | checkbox, slider, select_slider, text_input, number_input, date_input, time_input, text_area, color_picker |
        | index | int | Индекс выбранного элемента по умолчанию при визуализации | radio, selectbox |
        | options | iterable | Необязательные элементы компонента | radio, selectbox, multiselect, select_slider |
        | format_func | Имя функции | Функция форматирования опций | radio, selectbox, multiselect, select_slider |
        | min_value и max_value | int или float или date | допустимый диапазон значений | slider, number_input, date_input |
        | max_chars | int | Максимальное количество вводимых символов | text_input, text_area |
        | step | int или float | Длина шага | slider, number_input |
        | format |%. | Формат значения | slider,number_input |
        """)
p1t7t3 = ("""
        ###### 参数解释\n
        (1) **LABEL**： label是所有组件唯一**必须填写的参数**。对于按钮类组件，会显示在按钮内部；对于其他组件，会显示为组件上方的标签。\n
        (2) **KEY**：与其他GUI的'事件'相似，每个组件都应该被指定一个唯一的键名(key)，用于事件捕捉和响应。key是可选参数，如果不指定，当组件被创建时，Streamlit也会自动为其注册一个与label同名的key(但是不会写入session_state)。\n
                一般来说，包含但不限于下述情况需要由人工指定键名：\n
                1 你的应用存在多个标签名相同的组件（并且无法回避），导致默认键名冲突；\n
                2 你希望在session_state中写入组件的返回值，以便共享或调用。\n
        (3) **HELP**：组件的帮助文字。对于按钮类组件，会在鼠标悬停时显示在上方；对于其他组件，会在右上方显示一个圆圈问号标志，鼠标悬停在上方时显示。\n
                help参数可以为你的提示信息大大节约布局空间。你永远都猜不到你的应用的使用者会蠢得多么感人，如果你没有信心，可以加上必要的帮助信息。\n
        (4) **ON_CLICK 或 ON_CHANGE, \*ARGS, \*\*KWARGS**：\n
                Streamlit的组件都有返回值，可以直接调用，所以并不需要回调函数。但是，如果有特殊需求，你也可以为其指定回调函数。args和kwargs可以为其传递参数。\n
                一般来说，包含但不限于下述情况需要由人工指定回调函数：\n
                1 你迷恋于前后端分离，或者至少是前端和业务代码分离；\n
                2 你有多个组件指向同一个回调函数，并需要代码复用；\n
                3 你写的代码太骚气，有着复杂的逻辑而需要用到回调函数。\n
        (5) **VALUE** 和 **INDEX**：组件在渲染时的默认值，或者默认选择项的索引。对于单选型组件为index，对于其他类型组件为value。\n
        (6) **OPTIONS**：组件可供选择的选项，应该是序列或可迭代对象。适用于选择型组件。可以是列表、元组、np.ndarray、pd.series、pd.dataframe。如果是pd.dataframe，默认为第一列。\n
        (7) **FORMAT_FUNC**：用于将选项格式化处理的回调函数。一般来说，可以用于优化选项的文字显示，也可以通过字典来传入信息。\n
        (8) **MIN_VALUE & MAX_VALUE**：值域。限定组件的取值范围。\n
        (9) **MAX_CHARS**：最大字符数。限制文本输入的长度。\n
        (A) **STEP**：组件按钮调整的步长。\n
        (B) **FORMAT**：以何种格式显示组件的值。\n
        """,
        """
        ###### Parameters' explanation\n
        (1) **LABEL**: the only one **required parameter** for all components. For buttons it is displayed inside the button; for others, it is displayed as a label above the component. \n
        (2) **KEY**: Similar to other GUI's 'events', every component should be assigned a unique key name (called 'key') for event capture and response. The KEY is an optional parameter. If not specified, Streamlit will automatically register a key with the same name as the label when the component is created (but it will not be shown in session_state). \n
                Generally speaking, including but not limited to the following situations, the key name needs to be manually specified:\n
                1 There are multiple components with the same label name in your application (and cannot be avoided), causing the default key name conflict;\n
                2 You want to write the return value of a component in session_state for sharing or calling. \n
        (3) **HELP**: the help text of a component. For buttons, it will be displayed on the top of a button when the mouse is hovering; for others, a circle question mark will be displayed on the top right near the component, and help texts will be displayed when the mouse is hovering on the top. \n
                The help parameter can greatly save layout space for your prompt information. You can never imagine how stupid some users are. \n
                Provide some help information to stop them. \n
        (4) **ON_CLICK or ON_CHANGE, \*ARGS, \*\*KWARGS**:\n
                All streamlit components have return values ​​and can be called directly, so there is no requirement for callback functions. \n
                However, if you have special needs, you can also specify a callback function for them. And args and kwargs can pass parameters to the callback. \n
                Generally speaking, including but not limited to the following situations, the callback function needs to be manually specified:\n
                1 You are infatuated with the separation of front-end and back-end, or at least the separation of front-end and business code;\n
                2 You have multiple components that point to the same callback function and need code reuse;\n
                3 The code you wrote is very irritating, which has complicated logic and needs a callback function. \n
        (5) **VALUE** and **INDEX**: The default value of a component when rendering, or the index of the default selection. It is index for single-selection components, and value for other types of components. \n
        (6) **OPTIONS**: The options for the component to choose from, should be a sequence or an iterable. Its type can be list, tuple, np.ndarray, pd.series, pd.dataframe; first column as defualt if pd.dataframe.\n
        (7) **FORMAT_FUNC**: A callback function used to format options. Generally speaking, it can be used to optimize the text display of options, or to pass in information through a dictionary. \n
        (8) **MIN_VALUE & MAX_VALUE**: Valid value range. Limit the value range of the component. \n
        (9) **MAX_CHARS**: Maximum number of characters. Limit the length of text input. \n
        (A) **STEP**: The step length of the component changed by a single click. \n
        (B) **FORMAT**: In what format to display the value of the component. \n
        """,
        """
        ###### Объяснение параметров \n
        (1) ** LABEL **: единственный ** обязательный параметр ** для всех компонентов. Для кнопок он отображается внутри кнопки; для других он отображается как метка над компонентом. \n
        (2) ** KEY **: Подобно другим «событиям» графического интерфейса, каждому компоненту должно быть присвоено уникальное имя ключа (называемое «ключом») для захвата событий и ответа. KEY - необязательный параметр. Если не указано иное, Streamlit автоматически зарегистрирует ключ с тем же именем, что и метка, при создании компонента (но он не будет отображаться в session_state). \n
                Вообще говоря, включая, помимо прочего, следующие ситуации, имя ключа необходимо указывать вручную: \n
                1 В вашем приложении есть несколько компонентов с одинаковым именем метки (и этого нельзя избежать), что вызывает конфликт имени ключа по умолчанию; \n
                2 Вы хотите записать возвращаемое значение компонента в session_state для совместного использования или вызова. \n
        (3) ** HELP **: текст справки компонента. Для кнопок он будет отображаться в верхней части кнопки при наведении курсора мыши; для других в правом верхнем углу рядом с компонентом будет отображаться круговой вопросительный знак, а при наведении указателя мыши на него будут отображаться справочные тексты. \n
                Параметр справки может значительно сэкономить место на макете для вашей подсказки. Вы даже представить себе не можете, насколько глупы некоторые пользователи. Предоставьте некоторую справочную информацию, чтобы их остановить. \n
        (4) ** ON_CLICK или ON_CHANGE, \*ARGS, \*\*KWARGS **: \n
                Все компоненты streamlit имеют возвращаемые значения и могут быть вызваны напрямую, поэтому функции обратного вызова не требуются. \n
                Однако, если у вас есть особые потребности, вы также можете указать для них функцию обратного вызова. А args и kwargs могут передавать параметры обратному вызову. \n
                Вообще говоря, включая, помимо прочего, следующие ситуации, функцию обратного вызова необходимо указывать вручную: \n
                1 Вы увлечены разделением клиентской части и серверной части или, по крайней мере, разделением клиентского и бизнес-кода; \n
                2 У вас есть несколько компонентов, которые указывают на одну и ту же функцию обратного вызова и требуют повторного использования кода; \n
                3 Написанный вами код очень раздражает, имеет сложную логику и требует функции обратного вызова. \n
        (5) ** VALUE ** и ** INDEX **: значение по умолчанию для компонента при визуализации или индекс выбора по умолчанию. Это индекс для компонентов с одним выбором и значение для других типов компонентов. \n
        (6) ** OPTIONS **: параметры для выбора компонента должны быть последовательными или повторяемыми. Его тип может быть списком, кортежем, np.ndarray, pd.series, pd.dataframe; первый столбец по умолчанию, если pd.dataframe. \n
        (7) ** FORMAT_FUNC **: функция обратного вызова, используемая для форматирования параметров. Вообще говоря, его можно использовать для оптимизации текстового отображения параметров или для передачи информации через словарь. \n
        (8) ** MIN_VALUE & MAX_VALUE **: допустимый диапазон значений. Ограничьте диапазон значений компонента. \n
        (9) ** MAX_CHARS **: максимальное количество символов. Ограничьте длину ввода текста. \n
        (A) ** STEP **: длина шага компонента изменяется одним щелчком мыши. \n
        (B) ** FORMAT **: В каком формате отображать значение компонента. \n
        """)
p1t7t4 = ("###### 让我们看一个完整的示例",
          "###### Let's look at a complete example",
          "###### Давайте посмотрим на полный пример")
p1t7t5 = ("""
        接下来将展示各个组件的效果。\n
        为了让API更清晰，在所有组件中均存在的key、help、on_click、on_change、\*args、\*\*kwargs，会被省略。\n
        其他参数中前文已经提及的，也不会详细介绍。\n
        """,
        """
        Next, all components' examples will be shown. \n
        In order to make the API clear, the parameters(key, help, on_click, on_change, \*args, and \*\*kwargs) that exist in all components will be ignored. \n
        The other parameters that have been mentioned above will not be introduced in detail. \n
        """,
        """
        Далее будут показаны примеры всех компонентов. \n
         Чтобы сделать API понятным, параметры (key, help, on_click, on_change, \*args и \*\*kwargs), которые существуют во всех компонентах, будут проигнорированы. \n
         Остальные параметры, которые были упомянуты выше, не будут вводиться подробно. \n
        """)
p1t7t6 = ("在text_input中，type可以为default（普通）或password（密码）。autocomplete为自动填表内容。",
          "In st.text_input, 'type' can be 'default'(normal) or 'password'(for password). 'autocomplete' is the content of a form that automatically filled in.",
          "В st.text_input типом может быть default (обычный) или пароль (для пароля). ‘автозаполнение’ - это содержимое формы, которая заполняется автоматически.")
p1t7t7 = ("""
        data：要下载的对象。\n
        file_name：要显示的文件名称，如果不填会自动生成。\n
        MIME: 多用途互联网邮件拓展，参考[这里](https://www.w3school.com.cn/media/media_mimeref.asp)\n
        """,
        """
        data: The object to be downloaded. \n
        file_name: The name of the file to be displayed. Automatically generated if not given. \n
        MIME: Multipurpose Internet Mail Extension, please refer to [MIME](https://www.w3school.com.cn/media/media_mimeref.asp)\n
        """,
        """
        data: объект для загрузки. \n
         file_name: имя отображаемого файла. Если не указано, создается автоматически. \n
         MIME: многоцелевое расширение почты Интернета, см. [MIME] (https://www.w3school.com.cn/media/media_mimeref.asp) \n
        """)
p1t7t8 = ("type为文件类型，None为不限。accept_multiple_files是否可以上传多个文件。",
          "'type' means the file type, and None stands for unlimited. accept_multiple_files means whether uploading multiple files allowed.",
          "«тип» означает тип файла, а «Нет» означает неограниченный. accept_multiple_files означает, разрешена ли загрузка нескольких файлов.")
p1t8t1 = ("布局",
          "Layouts",
          "Макеты")
p1t8t2 = ("创建组件时，只需加上st.sidebar就可以将组件显示在侧栏。例如st.radio改为st.sidebar.radio。除了st.echo和st.spinner都支持。",
          "When creating a component, just add st.sidebar to display the component in the sidebar. For example, 'st.radio' is changed to 'st.sidebar.radio'. All components supported except 'st.echo' and 'st.spinner'.",
          "При создании компонента просто добавьте st.sidebar, чтобы отобразить компонент на боковой панели. Например, st.radio заменяется на st.sidebar.radio. Поддерживаются все компоненты, кроме st.echo и st.spinner.")
p1t8t3 = ("""
        st.columns可以实现类似Bootstrap的网格布局，可以将一行分为多列。\n
        参数：如果是整数n，则将该行平均分成n列；如果是序列，例如[3,2,1]，则将该行分为三列，各列的宽度分别为最大宽度的3/6、2/6、1/6。\n
        注意：1 移动终端会自动使用自适应模式，导致本功能失效。2 在目前版本中st.columns不能嵌套，即不能在某一列中嵌套使用st.columns。\n
        """,
        """
        st.columns supports a grid layout similar to Bootstrap, one single row can be divided into multiple columns. \n
        Parameter: If it is an integer N, that row will be divided into N columns equally; if it is a sequence(list or tuple), such as [3,2,1], the row will be divided into 3 columns, and the width of each column is 3/6, 2/6, 1/6 of the maximum width. \n
        Notice that: 1. Mobile devices will automatically use the adaptive mode, causing st.columns fail. 2. So far st.columns cannot be nested, that is, st.columns cannot be nested into a column. \n
        """,
        """
        st.columns поддерживает макет сетки, аналогичный Bootstrap, одна строка может быть разделена на несколько столбцов. \n
         Параметр: если это целое число N, эта строка будет разделена на N столбцов поровну; если это последовательность (список или кортеж), например [3,2,1], строка будет разделена на 3 столбца, а ширина каждого столбца составит 3/6, 2/6, 1/6 от максимальная ширина. \n
         Обратите внимание, что: 1. Мобильные устройства будут автоматически использовать адаптивный режим, что приведет к сбою st.columns. 2. Пока st.columns не могут быть вложенными, то есть st.columns не могут быть вложены в столбец. \n
         """)
p1t8t4 = ("你可以使用st.expander来隐藏不需要立刻展示的部分，以优化布局空间。请注意，即使st.expander在折叠状态下，其内部内容也会被渲染。所以，如果内容较多，还是建议更多地利用st.cache等功能分页处理。",
          "You can use st.expander to hide the parts no need to display to optimize the layout space. Please notice that even if a st.expander is at the collapsed state, its internal content will still be rendered. If there is too much content, it is recommended to use st.cache and other methods to split them into pages.",
          "Вы можете использовать st.expander, чтобы скрыть детали, которые не нужно отображать, чтобы оптимизировать пространство макета. Обратите внимание, что даже если st.expander находится в свернутом состоянии, его внутреннее содержимое все равно будет отображаться. Если контента слишком много, рекомендуется использовать st.cache и другие методы для разделения их на страницы.")
p1t8t5 = ("st.container是一个占位容器。Streamlit是自上而下渲染的。如果你需要调整对象显示的顺序，就可以先设置一个容器，然后将渲染后的内容写入容器里。",
          "st.container is a placeholder. Streamlit renders from top to bottom. If you need to change the display order of objects, you can set a container first, and then write the rendered content into the container.",
          "st.container - это заполнитель. Streamlit выполняет рендеринг сверху вниз. Если вам нужно изменить порядок отображения объектов, вы можете сначала установить контейнер, а затем записать визуализированный контент в контейнер.")
p1t8t6 = ("st.empty也是一个占位容器，不同的是，st.empty只接收“一个”对象的写入，再次写入会覆盖此前的内容。比如下面的案例（倒计时），就很适合用st.empty。",
          "st.empty is also a placeholder. Different from st.container, st.empty only accepts 'one' object write-in, and writing again will overwrite the previous one. As an example,  the countdown below is very suitable for st.empty. ",
          "st.empty также является заполнителем. В отличие от st.container, st.empty принимает только запись «одного» объекта, а повторная запись перезапишет предыдущий. Например, обратный отсчет ниже очень подходит для st.empty.")
p1t8t7 = ("控制流",
          "Control Flow",
          "Поток управления")
p1t8t8 = ("立刻结束程序。",
          "Terminate the program immediately.",
          "Немедленно завершите программу.")
p1t8t9 = ("""
        参数：key：表单键名（注意，必须指定）。clear_on_submit：是否在提交后清除表单内容。\n
        前面说过，Streamlit的组件状态变化会触发rerun。如果想同时提交一组数据时，普通的组件就不能用了。\n
        st.form也是一个容器，用法与st.container类似，可以用with语句，也可以链式调用。\n
        注意，在st.form中，只有st.form_submit_button允许有回调函数。\n
        """,
        """
        Parameters: \n
        Key: form's key name(must be given). clear_on_submit: Whether to clear the form after submission. \n
        As mentioned earlier, Components' state changes will trigger a rerun. It is hard if you want to submit a set of data at the same time. \n
        st.form is also a container. Similar to st.container, you can use the 'with' expression or chain-call. \n
        Notice that in a st.form, only st.form_submit_button can have a callback. \n
        """,
        """
        Параметры: \n
         Ключ: имя ключа формы (необходимо указать). clear_on_submit: очищать ли форму после отправки. \n
         Как упоминалось ранее, изменения состояния компонентов вызовут повторный запуск. Это сложно, если вы хотите отправить набор данных одновременно. \n
         st.form также является контейнером. Подобно st.container, вы можете использовать выражение «с» или цепной вызов. \n
         Обратите внимание, что в st.form только st.form_submit_button может иметь обратный вызов. \n
        """)
p1t8t10 = ("公共组件",
          "Utilities",
          "Утилиты")
p1t8t11 = ("通过st.set_page_config可以设置页面的部分属性。注意本句是初始化语句，只能出现在程序的第一句并且只能出现一次。",
          "You can set application's some attributes through st.set_page_config. Notice that this method is for initialization, which can only appear as the first line of a program and only once.",
          "Вы можете установить некоторые атрибуты приложения через st.set_page_config. Обратите внимание, что этот метод предназначен для инициализации, которая может отображаться только в первой строке программы и только один раз.")
p1t8t12 = ("""
        参数：\n
        如果参数不被设置，将使用Streamlit的默认属性。\n
        page_title：页面标题，str or None。\n
        page_icon：页面图标，st.image or [Emoji](https://www.emojipedia.org/)。\n
        layout：可以为centered或wide。如果是wide则为宽屏模式。建议在分辨率较低的情况下使用centered，并尽量减少复杂布局。\n
        initial_sidebar_state：在auto模式下，电脑端会自动显示sidebar，而移动端会隐藏sidebar。一般不需要修改。\n
        menu_items：应用右上角的功能框，可以加入你的自定义内容。\n
        """,
        """
        Parameters:\n
        If any parameter is not set, the default set of Streamlit will be used. \n
        page_title: page title, str or None. \n
        page_icon: page icon, st.image or [Emoji](https://www.emojipedia.org/). \n
        layout: can be 'centered' or 'wide'. If it is 'wide', it is in widescreen mode. It is recommended to use 'centered' when the resolution is low, and avoid complex layout. \n
        initial_sidebar_state: In auto mode, the computer will automatically display the sidebar, while the mobile terminal will hide the sidebar. Generally, no modification is required. \n
        menu_items: The function box at the top right corner of the application, you can add your custom content. \n
        """,
        """
        Параметры: \n
         Если какой-либо параметр не задан, будет использоваться набор Streamlit по умолчанию. \n
         page_title: заголовок страницы, str или None. \n
         page_icon: значок страницы, st.image или [Emoji] (https://www.emojipedia.org/). \n
         макет: может быть «по центру» или «по ширине». Если он «широкий», он находится в широкоэкранном режиме. Рекомендуется использовать «по центру» при низком разрешении и избегать сложной компоновки. \n
         initial_sidebar_state: в автоматическом режиме компьютер автоматически отображает боковую панель, а мобильный терминал скрывает ее. Как правило, никаких изменений не требуется. \n
         menu_items: Функциональное поле в правом верхнем углу приложения, вы можете добавить свой собственный контент. \n
        """)
p1t8t13 = ("使用with st.echo()语句，可以显示一组代码，并执行它。一般用于教学环境或文档。例如，本文档前面所呈现的内容就都是用st.echo实现的。",
          "Using 'with st.echo()', you can display a set of code and execute it. Usually used in teaching environments or documents. For example, the contents shown earlier in this document are almost all implemented by st.echo.",
          "Используя 'with st.echo ()', вы можете отобразить набор кода и выполнить его. Обычно используется в учебной среде или в документах. Например, содержимое, показанное ранее в этом документе, почти полностью реализовано st.echo.")
p1t9t1 = ("会话状态","Session State","Состояние сеанса")
p1t9t2 = ("下面介绍的是与缓存有关的功能。一是对会话状态的缓存st.session_state；二是对对象的缓存st.cache（以及优化版的st.memo、st.singleton）",
          "The following describes the functions related to caching. st.session_state is about user's session state;  st.cache (and optimized as st.memo or st.singleton) is about objects' cache.",
          "Ниже описаны функции, связанные с кешированием. st.session_state - о состоянии сеанса пользователя; st.cache (и оптимизированный как st.memo или st.singleton) касается кеша объектов.")
p1t9t3 = ("""
        每当使用一个浏览器标签访问Streamlit应用时，会创建一个独立的用户会话（user session）。\n
        前文提到，每当任意组件的状态发生变化时，会触发整个应用重新运行（rerun）。所有代码会自上而下重新运行，组件和对象都会重载。\n
        st.session_state可以用于解决对象值的共享问题。它的生命周期是自标签页渲染开始直至标签页关闭，不会受重新运行影响。\n
        下面展示了两个计数器案例，左侧的没有使用session_state，右侧的使用了session_state。分别点击两个按钮试试。\n
        """,
        """
        When you open a browser tab to access your Streamlit application, an user session is created. \n
        As mentioned earlier, whenever the state of any component changes, it will trigger the entire application to rerun. All code will rerun from top to bottom, and components and objects will be reloaded. \n
        st.session_state can be used to solve the problem of sharing objects' values. Its life period is from the start of page rendering to the page tab closed, and will not be affected by rerun. \n
        The following shows two counter examples, the left one didn't use session_state, and the right one used session_state. Click the buttons to try. \n
        """,
        """
        Когда вы открываете вкладку браузера для доступа к вашему приложению Streamlit, создается пользовательский сеанс. \n
         Как упоминалось ранее, всякий раз, когда состояние любого компонента изменяется, это вызывает перезапуск всего приложения. Весь код будет перезапущен сверху вниз, а компоненты и объекты будут перезагружены. \n
         st.session_state можно использовать для решения проблемы разделения значений объектов. Его период жизни - от начала рендеринга страницы до закрытия вкладки страницы, и повторный запуск на него не влияет. \n
         Ниже показаны два примера счетчиков: левый не использует session_state, а правый использует session_state. Нажмите кнопки, чтобы попробовать. \n
         """)
p1t9t4 = ("""
        在第一个案例中，由于存在'count=0'的初始化赋值，每次按钮被点击时，应用会重新运行，把变量count的值重置为0。这导致自增的效果无法实现。\n
        在第二个案例中，将count的值写入了st.session_state。每次按钮被点击时，应用会重新运行，但是count的值不会重置。\n
        """,
        """
        In the first case, due to the initial assignment of 'count=0', every time when the button is clicked, the application will re-run and reset the value of the variable 'count' to 0. This makes the self-increment impossible. \n
        In the second case, the value of 'count' is written into st.session_state. Every time when the button is clicked, the application will re-run, but the value of 'count' will not be reset. \n
        """,
        """
        В первом случае из-за начального присвоения «count = 0» каждый раз, когда нажимается кнопка, приложение будет повторно запускаться и сбрасывать значение переменной «count» на 0. Это приводит к самоприращению. невозможно. \n
         Во втором случае значение count записывается в st.session_state. Каждый раз, когда нажимается кнопка, приложение запускается повторно, но значение «count» не сбрасывается. \n
        """)
p1t9t5 = ("st.session_state是字典结构。所以，它的特性和字典完全一样，比如：",
          "st.session_state is dict-like. So it has many features almost the same as a dict, such as:",
          "st.session_state похож на dict. Таким образом, он имеет много функций, почти таких же, как dict, например:")
p1t9t6 = ("1. 和字典一样，有两种方法可以获取session_state中的键值：",
          "1. Like a dict, there are two ways to get a key's value in the session_state:",
          "1. Как и в случае с dict, есть два способа получить значение ключа в session_state:")
p1t9t7 = ("2. KEY在被调用前必须进行初始赋值。和字典一样，调用一个不存在的KEY会引发异常。通常我们可以这样做：",
          "2. A KEY must be initialized before called. Like a dict, calling a not-exist KEY will raise an exception. Usually we can do this:",
          "2. KEY должен быть инициализирован перед вызовом. Как и в случае с dict, вызов несуществующего KEY вызовет исключение. Обычно мы можем это сделать:")
p1t9t8 = ("3. 直接用st.session_state可以查看已经被创建的键。",
          "3. Use st.session_state to view all keys already created.",
          "3. Используйте st.session_state, чтобы просмотреть все уже созданные ключи.")
p1t9t9 = ("""
        其他关于st.session_state\n
        st.session_state只在会话被创建时重置（例如新建标签页访问Streamlit应用，或者刷新页面）。当浏览器标签页被关闭后，session_state就会失效。\n
        除了st.button和st.file_uploader，其他组件在创建时会自动添加一个键到st.session_state。\n
        不能使用st.session_state修改已经实例化（已渲染）的互动组件的值。\n
        """,
        """
        Others about st.session_state\n
        st.session_state is only reset when the user session is created (for example, when to open a new page tab to access the Streamlit application, or when to refresh the page). When the browser tab is closed, session_state becomes invalid. \n
        Except st.button and st.file_uploader, other components will automatically be added a key to st.session_state when they are created. \n
        You cannot use st.session_state to modify the value of an interactive component that has been instantiated (rendered). \n
        """,
        """
        Другое о st.session_state \n
         st.session_state сбрасывается только при создании сеанса пользователя (например, когда нужно открыть новую вкладку страницы для доступа к приложению Streamlit или когда обновить страницу). Когда вкладка браузера закрывается, session_state становится недействительным. \n
         За исключением st.button и st.file_uploader, другие компоненты будут автоматически добавлять ключ к st.session_state при их создании. \n
         Вы не можете использовать st.session_state для изменения значения интерактивного компонента, который был создан (визуализирован). \n
         """)
p1t9t10 = ("缓存： st.cache, st.memo, st.singleton",
          "Cache: st.cache, st.memo, st.singleton",
          "Кэш: st.cache, st.memo, st.singleton")
p1t9t11 = ("""
        Streamlit只能通过'streamlit run app.py'的方法启动。这意味着所有的功能都需要写在app.py的内部。\n
        想象一下，如果你需要诸如从本地路径或者网络URL打开一个文件、下载或上传文件、连接数据库、对一组数据进行固定步骤的预处理……每次rerun时都会执行一次。这太荒谬了。\n
        Streamlit可以启用缓存机制来完成以上动作，降低运行开销，直至会话结束。\n
        如果你用@st.cache装饰一个函数，它会检查函数名、函数体、参数，以及返回值，并将其哈希。每次rerun时，如果上述信息全部相同（哈希值相同），则使用缓存直接返回返回值。\n
        这对于我们上面提到的几种情况来说，会大大提升效率。但是，请注意数据的时效性，别忘了时间戳也是一个“看不见”的参数。例如，从网络上获取数据，数据可能在不同时间发生变化，导致你错过一些数据而影响计算结果。\n
        st.memo和st.singleton则是对st.cache的优化。[参考这里](https://blog.streamlit.io/new-experimental-primitives-for-caching/)
        简单地说，st.cache完成的缓存工作有两类：一类是对数据的计算（例如计算函数、本地文件的读写、数据表的计算和处理）；另一类是对非数据对象的执行和检查（比如连接数据库并保持、保持Tensorflow会话）。有时这些任务混合在一起，但是并不需要都进行，导致了一些不必要的开销。\n
        st.memo和st.singleton正是从st.cache中细化而来的。\n
        st.memo是用来处理返回数据的函数的，也就是前面提到的第一类，这也是我们最常用到的缓存功能；\n
        st.singleton是用来处理非数据对象（例如保持会话、保持数据库连接）的。\n
        根据官方博客的介绍，st.memo的效率远高于st.cache。如果想了解更多信息，请参考[官方API文档](https://docs.streamlit.io/)。
        """,
        """
        Streamlit can only be started via the 'streamlit run app.py' method. It means that all functions need to be written inside app.py. \n
        Just imagine if you need to: open a file from a local path or a web URL, download or upload a file, connect to a database, preprocess a fixed dataset...they will be executed in every rerun. That is ridiculous. \n
        Streamlit can enable the caching mechanism to make the actions mentioned above and reduce operating cost until the session ends. \n
        If you decorate a function with @st.cache, it will check: the function name, function body, parameters, and return value, and hash them. In each rerun, if these information is all the same (the hash value is the same), the cache is used to directly return the return value. \n
        This will greatly improve efficiency for the several situations we mentioned above. However, please keep attention to the timeliness of the data, and don't forget that the timestamp is also an "invisible" parameter. For example, when you get data from the Internet, the data may change at different times, causing you to miss some data and affect the calculation results. \n
        st.memo and st.singleton are optimizations of st.cache. [Blog reference here](https://blog.streamlit.io/new-experimental-primitives-for-caching/)
        Simply, there are two types of caching work done by st.cache: the one is the calculation of data (such as calculation functions, reading and writing of local files, calculation and processing of dataframes); the other is for non-data objects' status (such as connecting to a database and maintaining, maintaining a Tensorflow session). Sometimes these tasks are mixed together, but not all of them need to be execuated, which may bring some unnecessary cost. \n
        st.memo and st.singleton are refined from st.cache. \n
        st.memo is a function used to check the objects that return data ( the first type mentioned earlier), which is more commonly used cache method;\n
        st.singleton is used to handle non-data objects (such as maintaining sessions, maintaining database connections). \n
        According to the introduction of the official blog, the efficiency of st.memo is much higher than that of st.cache. For more information, please refer to [Official API Documentation](https://docs.streamlit.io/).
        """,
        """
        Streamlit можно запустить только с помощью метода streamlit run app.py. Это значит, что все функции нужно писать внутри app.py. \n
        Только представьте, если вам нужно: открыть файл по локальному пути или веб-URL, загрузить или загрузить файл, подключиться к базе данных, предварительно обработать фиксированный набор данных ... они будут выполняться при каждом повторном запуске. Это смешно. \n
        Streamlit может включить механизм кэширования для выполнения упомянутых выше действий и снизить эксплуатационные расходы до завершения сеанса. \n
        Если вы украсите функцию @ st.cache, она проверит: имя функции, тело функции, параметры и возвращаемое значение и хеширует их. При каждом повторном запуске, если эта информация одинакова (хеш-значение одинаково), кэш используется для непосредственного возврата возвращаемого значения. \n
        Это значительно повысит эффективность в нескольких вышеупомянутых ситуациях. Однако обратите внимание на своевременность данных и не забывайте, что отметка времени также является «невидимым» параметром. Например, когда вы получаете данные из Интернета, они могут изменяться в разное время, в результате чего вы пропустите некоторые данные и повлияете на результаты расчетов. \n
        st.memo и st.singleton - это оптимизации st.cache. [Ссылка на блог здесь] (https://blog.streamlit.io/new-experimental-primitives-for-caching/)\n
        Проще говоря, st.cache выполняет два типа кэширования: первый - это вычисление данных (например, функции вычисления, чтение и запись локальных файлов, вычисление и обработка фреймов данных); другой - для состояния объектов, не относящихся к данным (например, подключение к базе данных и поддержка, поддержание сеанса Tensorflow). Иногда эти задачи смешиваются, но не все из них нужно выполнять, что может привести к ненужным расходам. \n
        st.memo и st.singleton улучшены из st.cache. \n
        st.memo - это функция, используемая для проверки объектов, возвращающих данные (первый тип, упомянутый ранее), что является более часто используемым методом кеширования; \n
        st.singleton используется для обработки объектов, не относящихся к данным (таких как поддержание сеансов, поддержание соединений с базой данных). \n
        Согласно введению официального блога, эффективность st.memo намного выше, чем у st.cache. Для получения дополнительной информации см. [Официальная документация по API] (https://docs.streamlit.io/).
        """)