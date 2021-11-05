import streamlit as st
from lang_text import *
# page config
st.set_page_config(page_title="Streamlit Experience",layout="wide")
# init vars
st.session_state.la_s = 0
langs = ("简体中文","English","Русский")

# Sidebar
lang_select = st.sidebar.radio("请选择语言 Please Select Your Language",langs)
if lang_select == "简体中文":
    st.session_state.la_s = 0
elif lang_select == "English":
    st.session_state.la_s = 1
elif lang_select == "Русский":
    st.session_state.la_s = 2
# las means language selector
las = st.session_state.la_s
# Page Selector
page = st.sidebar.selectbox(sbar_sbox_0[las],p_names[las])
# header
def write_header():
    r1c1,r1c2 = st.columns([9,6])
    with r1c1:
        f"# {header[las]}"
        f"#### {author[las]} (1.1.0.20211105)"
        st.warning(header_warning[las])
    with r1c2:
        if las == 0:
            st.image("buyme.png",width=100,caption="打赏流老湿")
        else:
            st.image("buyme.png",width=100,caption="Buy me Coffee")
        
if page == p_names[las][0]:
    write_header()
    "---"
    f"## {p_names[las][0]}"
    st.markdown(p0intro[las])

if page == p_names[las][1]:
    write_header()
    "---"
    f"## {p_names[las][1]}"
    p1t0[las]
    sel = st.selectbox(p1sbox0[las],p1sbox1[las])
    if sel == p1sbox1[las][0]: # Magic Commands
        f"#### {p1sbox1[las][0]}"
        p1t1t1[las]
        "---"
        r2c1,r2c2 = st.columns([6,6])
        with r2c1:
            f"##### (1) {p1t1t2[las]}"
            with st.echo():
                var_demo = 123456789
                var_demo
            st.success(p1t1t3[las])
        with r2c2:
            "##### (2) st.write(*args, **kwargs)"
            st.code("st.write(Object,[opt]unsafe_allow_html:bool=False)")
            with st.echo():
                st.write("#### This is #4 title.")
            st.warning(p1t1t4[las])
    if sel == p1sbox1[las][1]: # Display Text
        f"#### {p1sbox1[las][1]}"
        p1t2t1[las]
        "---"
        "##### (1) st.markdown"
        r3c1,r3c2 = st.columns([6,6])
        with r3c1:
            st.code("st.markdown(body:str, unsafe_allow_html:bool = False)")
            with st.echo():
                st.markdown("This is __*MARKDOWN*__") # Markdown
            with st.echo():
                st.markdown("<p style='color:red'>I am RED!</p>",True) # HTML
        with r3c2:
            p1t2t2[las]
        "---"
        "##### (2) st.title, st.header, st.subheader"
        r4c1,r4c2 = st.columns([6,6])
        with r4c1:
            st.code("""
            st.title(body:str, anchor:str = None)
            st.header(body:str, anchor:str = None)
            st.subheader(body:str, anchor:str = None)""")
            with st.echo():
                st.title("I am #1 title.") # equals "# text"
                st.header("I am #2 header.") # equals "## text"
                st.subheader("I am #3 subheader.") # equals "### text"
                # Markdown supports #1 - #6.
        with r4c2:
            p1t2t3[las]
        "---"
        "##### (3) st.caption"
        r5c1,r5c2 = st.columns([6,6])
        with r5c1:
            st.code("st.caption(body:str)")
            with st.echo():
                st.caption('This is a caption that explains something above.')
        with r5c2:
            p1t2t4[las]
        "---"
        "##### (4) st.code"
        r6c1,r6c2 = st.columns([6,6])
        with r6c1:
            st.code("st.code(body:str, language='python')")
            with st.echo():
                # 方法一
                st.code("mylist = [i for i in range(10)]") 
                # 方法二
                """```python 
                mylist = [i for i in range(10)]"""
        with r6c2:
            p1t2t5[las]
        "---"
        "##### (5) st.text"
        r7c1,r7c2 = st.columns([6,6])
        with r7c1:
            st.code("st.text(body:str)")
            with st.echo():
                st.text("This is sttext normal text.") 
                "This is markdown normal text."
                # Funny that they are different. Which one do you prefer?
        with r7c2:
            p1t2t6[las]
        "---"
        "##### (6) st.latex"
        r8c1,r8c2 = st.columns([6,6])
        with r8c1:
            st.code("st.latex(body:str)")
            with st.echo():
                st.latex(r"a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} = \sum_{k=0}^{n-1} ar^k = a \left(\frac{1-r^{n}}{1-r}\right)")
                r"$a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} = \sum_{k=0}^{n-1} ar^k = a \left(\frac{1-r^{n}}{1-r}\right)$" 
        with r8c2:
            p1t2t7[las]   
    if sel == p1sbox1[las][2]: # Display Data
        f"#### {p1sbox1[las][2]}"
        p1t3t1[las]
        "---"
        "##### (1) st.dataframe, st.table, Markdown Table"
        r9c1,r9c2,r9c3 = st.columns([6,6,6])
        with r9c1:
            st.code("st.dataframe(data=None, width=None, height=None)")
        with r9c2:
            st.code("st.table(data=None)")
        with st.echo():
            import numpy as np
            import pandas as pd
            df = pd.DataFrame(np.random.randn(5,5),columns=(str(i) for i in range(5)))
        r10c1,r10c2 = st.columns([6,6])
        with r10c1:
            with st.echo():
                "###### This is dataframe"
                st.dataframe(df.style.highlight_max(axis=1),900,300)
        with r10c2:
            with st.echo():
                "###### This is table"
                st.table(df)
        r11c1,r11c2 = st.columns([8,4])
        with r11c1:
            with st.echo():
                "###### This is Markdown table"
                md_table = """
                | 0 | 1 | 2 | 3 | 4 |
                | --- | --- | --- | --- | --- |
                """
                for i in range(len(df)):
                    md_table += f"| {df.iloc[i][0]} | {df.iloc[i][1]} | {df.iloc[i][2]} | {df.iloc[i][3]} | {df.iloc[i][4]} |\n"  
                md_table
        with r11c2:
            st.info(p1t3t2[las])
        "---"
        "##### (2) st.metric"
        st.code("st.metric(label:str, value:int/float/str/None, delta:int/float/str/None=None, delta_color:str='normal')")
        p1t3t3[las]
        with st.echo():
            r12c1,r12c2,r12c3,r12c4 = st.columns([6,6,6,6])
            with r12c1: # a simple example
                st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
            with r12c2: # render a line when value is None
                st.metric(label="Number1", value=None, delta="-15")
            with r12c3: # red up and green down
                st.metric(label="Number2", value=666,delta=166,delta_color="inverse")
            with r12c4: # color off
                st.metric(label="HelloWorld",value="刘志昱",delta="说",delta_color="off")
        "---"
        "##### (3) st.json"
        r13c1,r13c2 = st.columns([6,6])
        with r13c1:
            st.code("st.json(body:Object/str)")
            with st.echo():
                st.json({"name":"Viktor Liu",
                        "gender":"male",
                        "nation":"PR China",
                        "favor":["gruppa krovi","zvezdoy pa imeni solntse","pachka sigaret"]})
        with r13c2:
            p1t3t4[las]
    if sel == p1sbox1[las][3]: # Display Chart
        f"#### {p1sbox1[las][3]}"
        p1t4t1[las]
        "---"
        "##### (1) Built-in st.line_chart, st.area_chart, st.bar_chart"
        st.code("""
        st.line_chart(data=None, width:int=0, height:int=0, use_container_width:bool=True)
        st.area_chart(data=None, width:int=0, height:int=0, use_container_width:bool=True)
        st.bar_chart(data=None, width:int=0, height:int=0, use_container_width:bool=True)
        """)
        p1t4t2[las]
        with st.echo():
            import numpy as np
            import pandas as pd
            df = pd.DataFrame(np.random.randn(20,3),columns=["A","B","C"])
            "###### 这是折线图 This is line chart"
            st.line_chart(df)
            "###### 这是面积图 This is area chart"
            st.area_chart(df)
            "###### 这是棒棒图 This is bar chart"
            st.bar_chart(df)
        "---"
        "##### (2) st.map"
        st.code("st.map(data=None, zoom=None, use_container_width=True)")
        p1t4t3[las]
        with st.echo():
            import numpy as np
            import pandas as pd
            df = pd.DataFrame(np.random.randn(200,2) / [50,50] + [39.81819,119.48165],columns=["lat","lon"])
            st.map(df,zoom=11) # Welcome to Beidaihe!Try zoom in and out (by mouse wheel up and down)!
        "---"
        f"##### (3) {p1t4t4[las]}"
        p1t4t5[las]
        st.code("""
        st.pyplot(fig=None, clear_figure=None, **kwargs) # matplotlib
        st.altair_chart(altair_chart, use_container_width=False) # altair
        st.vega_lite_chart(data=None, spec=None, use_container_width=False, **kwargs) # vega lite
        st.plotly_chart(figure_or_data, use_container_width=False, sharing='streamlit', **kwargs) # plotly
        st.bokeh_chart(figure, use_container_width=False) # bokeh
        st.pydeck_chart(pydeck_obj=None, use_container_width=False) # pydeck
        st.graphviz_chart(figure_or_dot, use_container_width=False) # graphviz
        """)
    if sel == p1sbox1[las][4]: # Display Media
        f"#### {p1sbox1[las][4]}"
        p1t5t1[las]
        "---"
        "##### (1) st.image"
        st.code("st.image(image, caption=None, width=None, use_column_width=None, clamp=False, channels='RGB', output_format='auto')")
        r15c1,r15c2,r15c3 = st.columns([6,3,9])
        r14c1,r14c2 = st.columns([6,6])
        with r14c2:
            p1t5t2[las]
        with r14c1:
            with st.echo():
                # Code by jollysoul
                import random
                import numpy as np
                with r15c1:
                    r15form = st.form("r15form")
                    num_rows = int(r15form.number_input("请输入行数 Input Rows：",1,100,20,1))
                    num_cols = int(r15form.number_input("请输入列数 Input Columns：",1,100,20,1))
                    if r15form.form_submit_button("画迷宫 Draw Maze"):
                        M = np.zeros((num_rows,num_cols,5), dtype=np.uint8)
                        image = np.zeros((num_rows*10,num_cols*10), dtype=np.uint8)
                        r = 0
                        c = 0
                        history = [(r,c)]
                        while history: 
                            M[r,c,4] = 1
                            check = []
                            if c > 0 and M[r,c-1,4] == 0:
                                check.append('L')  
                            if r > 0 and M[r-1,c,4] == 0:
                                check.append('U')
                            if c < num_cols-1 and M[r,c+1,4] == 0:
                                check.append('R')
                            if r < num_rows-1 and M[r+1,c,4] == 0:
                                check.append('D')
                                
                            if len(check):
                                history.append([r,c])
                                move_direction = random.choice(check)
                                if move_direction == 'L':
                                    M[r,c,0] = 1
                                    c = c-1
                                    M[r,c,2] = 1
                                if move_direction == 'U':
                                    M[r,c,1] = 1
                                    r = r-1
                                    M[r,c,3] = 1
                                if move_direction == 'R':
                                    M[r,c,2] = 1
                                    c = c+1
                                    M[r,c,0] = 1
                                if move_direction == 'D':
                                    M[r,c,3] = 1
                                    r = r+1
                                    M[r,c,1] = 1
                            else:
                                r,c = history.pop()
                        M[0,0,0] = 1
                        M[num_rows-1,num_cols-1,2] = 1
                        for row in range(0,num_rows):
                            for col in range(0,num_cols):
                                cell_data = M[row,col]
                                for i in range(10*row+2,10*row+8):
                                    image[i,range(10*col+2,10*col+8)] = 255
                                if cell_data[0] == 1: 
                                    image[range(10*row+2,10*row+8),10*col] = 255
                                    image[range(10*row+2,10*row+8),10*col+1] = 255
                                if cell_data[1] == 1: 
                                    image[10*row,range(10*col+2,10*col+8)] = 255
                                    image[10*row+1,range(10*col+2,10*col+8)] = 255
                                if cell_data[2] == 1: 
                                    image[range(10*row+2,10*row+8),10*col+9] = 255
                                    image[range(10*row+2,10*row+8),10*col+8] = 255
                                if cell_data[3] == 1: 
                                    image[10*row+9,range(10*col+2,10*col+8)] = 255
                                    image[10*row+8,range(10*col+2,10*col+8)] = 255
                        with r15c3:
                            st.image(image,caption=f"{num_rows} x {num_cols} 迷宫")
        f"###### {p1t5t3[las]}"
        st.code("""
                from PIL import Image
                st.image(Image.open('filename.jpg',**kwargs))
                """)
        "---"
        "##### (2) st.video, st.audio"
        r16c1,r16c2 = st.columns([6,6])
        with r16c1:
            st.code("""
                    st.video(data, format='video/mp4', start_time=0)
                    st.audio(data, format='audio/wav', start_time=0)"
                    """)
            f"###### {p1t5t5[las]}"
            st.code("""
                    # videos
                    st.video(open('filename.mp4', 'rb').read(),**kwargs)
                    # audios
                    st.audio(open('filename.ogg', 'rb').read(), 
                                  format='audio/ogg', **kwargs)
                    """)
        with r16c2:
            p1t5t4[las]
    if sel == p1sbox1[las][5]: # Display Status
        f"#### {p1sbox1[las][5]}"
        p1t6t1[las]
        "---"
        "##### (1) st.info, st.success, st.warning, st.exception, st.error"
        r17c1,r17c2 = st.columns([4,8])
        with r17c1:
            """
            ```python
            st.info(body:str)
            st.success(body:str)
            st.warning(body:str)
            st.exception(Exception)
            st.info(body:str)
            ```
            """
            p1t6t2[las]
        with r17c2:
            with st.echo():
                st.info("On ne pomnit slova 'da' i slova 'net' 他不记得“是”和“否”两个词")
                st.success("On ne pomnit ni chinov, ni imen 他不记得军衔和荣誉")
                st.warning("I spasoben datjanut'snja da zvezd 他本以为可以摘到星星")
                st.exception(NameError("Ne schitaja, chto eta son 不曾想，这只是个梦"))
                st.error("I upast, opalennim zvezdoy pa imeni solntse 他坠落，被焚尽，被那颗，名为太阳的星辰")        
        "---"
        "##### (2) st.balloons"
        st.code("st.balloons()")
        p1t6t3[las]
        "---"
        "##### (3) st.progress, st.spinner"
        st.code("""
                st.progress(value:int or float)
                st.spinner(text：str = 'In progress...')
                """)
        p1t6t4[las]
        "###### Progress"
        with st.echo():
            import time
            bar = st.progress(0.0)
            for percentage in range(20):
                time.sleep(0.1)
                bar.progress(percentage * 0.05 + 0.05)
        "###### Spinner"
        with st.echo():
            with st.spinner('Wait for it...'):
                time.sleep(5)
            st.success('Done!')            
        
if page == p_names[las][2]:
    write_header()
    "---"
    f"## {p_names[las][2]}"
    p1t7t1[las]
    "---"
    p1t7t2[las]
    "---"
    p1t7t3[las]
    "---"
    p1t7t4[las]
    with st.echo():
        con = st.container()
        def callback():
            pass
        myradio = st.radio(label = "这是单选框", 
                           options = ("A","B","C"), # 选项 
                           index = 1, # 初始化选项
                           format_func = lambda x : f"这是选项{x}", #这是格式化函数，注意我把原始选项ABC修改了。一般地，跟字典或dataframe结合也很好用。
                           key = "radio_demo", 
                           help = "我是帮助文字", # 看到组件右上角的问号了没？上去悬停一下。
                           on_change = callback, args = None, kwargs = None)
        
        if myradio:
            con.write(f"你选择了{myradio} 它的session_state是{st.session_state.radio_demo}")
    "---"
    p1t7t5[las]
    "---"
    r18c1, r18c2 = st.columns([6,6])
    with r18c1:
        "###### (1) st.button 按钮"
        st.code("st.button(label) -> bool")
        with st.echo():
            if st.button("点我！"):
                "你点击了按钮！"
    with r18c2:
        "###### (2) st.checkbox 检查框"
        st.code("st.checkbox(label, value=False) -> bool")
        with st.echo():
            if st.checkbox("打勾了吗？"):
                "选中啦！"
            else:
                "没选中。"
    "---"
    r19c1, r19c2 = st.columns([6,6])
    with r19c1:
        "###### (3) st.radio 单项选择框"
        st.code("st.radio(label, options, index=0, format_func=None) -> str")
        with st.echo():
            my_radio = st.radio("你最喜欢哪首歌？",
                               ("pachka sigaret","gruppa krovi","zvezda pa imeni solntse"))
            if my_radio:
                f"我最喜欢{my_radio}"
    with r19c2:
        "###### (4) st.selectbox 下拉选择框"
        st.code("st.selectbox(label, options, index=0, format_func=None) -> str")
        with st.echo():
            my_selectbox = st.selectbox("Which song do you like most？",
                                ("pachka sigaret","gruppa krovi","zvezda pa imeni solntse"))
            if my_selectbox:
                f"I like {my_selectbox} most."
    "---"
    r20c1, r20c2 = st.columns([6,6])
    with r20c1:
        "###### (5) st.multiselect 多项选择框"
        st.code("st.multiselect(label, options, default=None, format_func=None) -> List[str]")
        with st.echo():
            my_multiselect = st.multiselect("选择你喜欢的歌",
                                        options=("《一包香烟》","《血型》","《名为太阳的星辰》"),
                                        default=("《一包香烟》","《血型》"))
            if my_multiselect:
                f"我喜欢 {'、'.join(i for i in my_multiselect)}。"
    with r20c2:
        "###### (6) st.text_area 多行文本框"
        st.code("st.text_area(label, value='', height=None, max_chars) -> str")
        with st.echo():
            st.text_area("Text Area Height = 200 pixels",
                         f"{' '.join(str(i) for i in range(200))}",
                         height=200)
    "---"
    r21c1, r21c2 = st.columns([6,6])
    with r21c1:
        "###### (7) st.slider & st.select_slider 滑杆、选项滑杆"
        st.code("st.slider(label, min_value, max_value, value, step, format=None)")
        st.code("st.select_slider(label, options, value=None, format_func=None")
        with st.echo():
            # 滑杆
            my_slider = st.slider("计算平方数",0,100,50,1)
            if my_slider:
                f"{my_slider}的平方是{my_slider ** 2}"
            # 选项滑杆
            transdict = {"Red":"红","Orange":"橙","Yellow":"黄",
                         "Green":"绿","Blue":"蓝","Purple":"紫"}
            my_select_slider = st.select_slider("Choose Your Favorite Color！",
                                    ("Red","Orange","Yellow","Green","Blue","Purple"),"Red")
            if my_select_slider:
                f"你选择了{transdict[my_select_slider]}色！"
    with r21c2:
        "###### (8) st.text_input, st.number_input, st.date_input, st.time_input 信息输入"
        st.code("""
        st.text_input(label, value='', max_chars=None, 
                      type='default', autocomplete=None) -> str
        st.number_input(label, min_value, max_value, 
                      value, step, format=None) -> int or float
        st.date_input(label, value, min_value, max_value) -> datetime.date
        st.time_input(label, value) -> datetime.time
        """)
        p1t7t6[las]
        with st.echo():
            st.text_input("这是TEXT_INPUT")
            st.number_input("这是NUMBER_INPUT",value=10)
            st.date_input("这是DATE_INPUT")
            st.time_input("这是TIME_INPUT")
    "---"
    r22c1, r22c2 = st.columns([6,6])   
    with r22c1:
        "###### (9) st.download_button 下载按钮"
        st.code("st.download_button(label, data, file_name=None, mime=None) -> bool")
        p1t7t7[las]
        """
        ```python
        # 1
        @st.cache
        def convert_df(df):
            return df.to_csv().encode('utf-8')    
        csv = convert_df(my_large_df)
        st.download_button(label="Download data as CSV", 
                        data=csv, file_name='large_df.csv', mime='text/csv')
        # 2
        text_contents = '''This is some text'''
        st.download_button('Download some text', text_contents)
        # 3
        binary_contents = b'example content'
        # MIME default as 'application/octet-stream'
        st.download_button('Download binary file', binary_contents)
        # 4
        with open("flower.png", "rb") as file:
            btn = st.download_button(label="Download image",
                                data=file,file_name="flower.png",mime="image/png")
        ```
        """
    with r22c2:
        "###### (10) st.file_uploader 文件上传"
        st.code("st.file_uploader(label, type=None, accept_multiple_files=False)")
        p1t7t8[las]
        """
        ```python
        # 上传单个文件 Upload single file
        uploaded_file = st.file_uploader("Choose a file")
        if uploaded_file is not None:
            # To read file as bytes:
            bytes_data = uploaded_file.getvalue()
            st.write(bytes_data)

            # To convert to a string based IO:
            stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
            st.write(stringio)

            # To read file as string:
            string_data = stringio.read()
            st.write(string_data)

            # Can be used wherever a "file-like" object is accepted:
            dataframe = pd.read_csv(uploaded_file)
            st.write(dataframe)

        #上传多个文件 Upload multi files
        uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
        for uploaded_file in uploaded_files:
            bytes_data = uploaded_file.read()
            st.write("filename:", uploaded_file.name)
            st.write(bytes_data)
        ```
        """
    "---"
    r23c1, r23c2 = st.columns([6,6])
    with r23c1:
        "###### (11) st.color_picker 拾色器"
        st.code("st.color_picker(label, value=None) -> str")
        with st.echo():
            color = st.color_picker('选择颜色', '#00f900')
            st.write('当前的颜色值是', color)

if page == p_names[las][3]:
    write_header()
    "---"
    f"## {p_names[las][3]}"
    "---"
    f"#### {p1t8t1[las]}"
    "---"
    r26c1, r26c2 = st.columns([6,6])
    with r26c1:
        "###### (1) st.sidebar 侧边栏"
        p1t8t2[las]
    with r26c2:
        "###### (2) st.expander 折叠栏"
        st.code("st.expander(label: str, expanded: bool = False)")
        p1t8t4[las]
        with st.echo():
            with st.expander("点击查看内部内容",False):
                st.success("这是内部的内容")
    "---"
    "###### (3) st.columns 多列布局"
    st.code("st.columns(spec: Union[int, Sequence[Union[int, float]]])")
    p1t8t3[las]
    with st.echo():
        r24c1,r24c2,r24c3 = st.columns(3)
        with r24c1:
            st.info("这是第一列")
        with r24c2:
            st.info("这是第二列")
        with r24c3:
            st.info("这是第三列")
        r25c1,r25c2,r25c3 = st.columns([3,2,1])
        with r25c1:
            st.success("这是第一列")
        with r25c2:
            st.warning("这是第二列")
        with r25c3:
            st.error("这是第三列")
    "---"
    r27c1, r27c2 = st.columns([6,6])
    with r27c1:
        "###### (4) st.container 容器"
        st.code("st.container()")
        p1t8t5[las]
        with st.echo():
            container = st.container()
            container.write("This is inside the container")
            st.write("This is outside the container")
            container.write("This is inside too")
    with r27c2: 
        "###### (5) st.empty 单一元素空容器"
        st.code("st.empty()")
        p1t8t6[las]
        with st.echo():
            import time
            with st.empty():
                for seconds in range(3):
                    st.write(f"⏳ {seconds} seconds have passed")
                    time.sleep(1)
                st.write("✔️ Done!")
    "---"
    f"#### {p1t8t7[las]}"
    "---"
    r28c1, r28c2 = st.columns([6,6])
    with r28c1:
        "###### (1)st.stop"
        p1t8t8[las]
        st.code("""
        name = st.text_input('Name')
        if not name:
            st.warning('Please input a name.')
            st.stop() # quit
        st.success('Thank you for inputting a name.')
        """)
    with r28c2:
        "###### (2) st.form st.form_submit_button 表单与表单提交按钮"
        st.code("""
        st.form(key: str, clear_on_submit: bool = False)")
        st.form_submit_button(label='Submit') -> bool
        """)
        p1t8t9[las]
        with st.echo():
            with st.form("calc"):
                num_1 = st.number_input("请输入第一个数",value=10)
                num_2 = st.number_input("请输入第二个数",value=10)
                if st.form_submit_button("计算乘积"):
                    f"两个数的乘积是{num_1 * num_2}"        
    "---"
    f"#### {p1t8t10[las]}"
    "---"
    "###### (1) st.set_page_config 页面设置"
    st.code("st.set_page_config(page_title=None, page_icon=None, layout='centered', initial_sidebar_state='auto', menu_items=None)")
    p1t8t11[las]
    p1t8t12[las]
    "---"
    "###### (2) st.echo 显示代码并运行"
    st.code("st.echo(code_location='above')")
    p1t8t13[las]
    st.code("""
    with st.echo():
        st.write('This code will be printed')
    """)
    "---"
    "###### (3) st.help 查询帮助文档"
    st.code("st.help(obj)")
    with st.echo():
        # st.help方法
        st.help(st.button)
        # 也可以用魔术方法直接写st.button

if page == p_names[las][4]:
    write_header()
    "---"
    f"## {p_names[las][4]}"
    p1t9t2[las]
    "---"
    f"#### {p1t9t1[las]}"
    p1t9t3[las]
    r29c1, r29c2 = st.columns([6,6])
    with r29c1:
        with st.echo():
            "###### Counter #1"
            count = 0
            increment = st.button('count++',key="ssdemo_0")
            if increment:
                count += 1
            st.write('Count = ', count)
    with r29c2:
        with st.echo():
            "###### Counter #2"
            if "count" not in st.session_state:
                st.session_state.count = 0
            increment = st.button('count++',key="ssdemo_1")
            if increment:
                st.session_state.count += 1
            st.write('Count = ', st.session_state.count)
    p1t9t4[las]
    st.info(p1t9t5[las])
    p1t9t6[las]
    st.code("""
            st.session_state.KEY") 
            st.session_state['KEY']
            """) 
    p1t9t7[las]
    st.code("""
        if "KEY" not in st.session_state:
            st.session_state.KEY = 0              
            """)
    p1t9t8[las]
    with st.echo():
        st.session_state #查看当前的session_state
    st.success(p1t9t9[las])
    "---"
    f"#### {p1t9t10[las]}"
    st.code("""
    st.cache(func=None, persist=False, allow_output_mutation=False, show_spinner=True, suppress_st_warning=False, hash_funcs=None, max_entries=None, ttl=None)
    st.memo(func = None, persist = None, show_spinner = True, suppress_st_warning=False, max_entries = None, ttl = None)
    st.singleton(func = None, show_spinner = True, suppress_st_warning=False)
    """)
    p1t9t11[las]