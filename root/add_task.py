import flet as ft
import datetime as dt

class ControllerNameBar(ft.UserControl):
    def build(self):
        _name_bar = ft.Container(height=60, alignment=ft.alignment.center,
                 padding=ft.padding.all(5), content=
                 ft.Container(bgcolor='#ffffff', border_radius=ft.border_radius.all(20),
                      content=ft.TextField(label='Your habit name',
                           border_radius=ft.border_radius.all(20), width=310,
                           border_color='#ffffff')))
        return _name_bar


class ControllerSelectDay(ft.UserControl):
    def build(self):

        def select_day_hover(e):
            if e.control.bgcolor != ft.colors.BLACK:
                if e.data == 'true':
                    e.control.bgcolor = ft.colors.BLACK12
                else:
                    e.control.bgcolor = '#ffffff'
                e.control.update()

        def select_day_click(e):
            if e.control.bgcolor in ['#ffffff', ft.colors.BLACK12]:
                # Active
                e.control.bgcolor = ft.colors.BLACK
                e.control.content.color = ft.colors.WHITE
                e.control.update()
            else:
                e.control.bgcolor = '#ffffff'
                e.control.content.color = ft.colors.BLACK
                e.control.update()

        _select_day = ft.Container(height=60, content=
        ft.Row(spacing=7, alignment=ft.MainAxisAlignment('center'), controls=[
            ft.Container(width=40, height=50, border_radius=ft.border_radius.all(80),
                         on_hover=lambda e: select_day_hover(e),
                         on_click=lambda e: select_day_click(e), alignment=ft.alignment.center, bgcolor='#ffffff',
                         content=ft.Text('Sun')),
            ft.Container(width=40, height=50, border_radius=ft.border_radius.all(80),
                         on_hover=lambda e: select_day_hover(e),
                         on_click=lambda e: select_day_click(e), alignment=ft.alignment.center, bgcolor='#ffffff',
                         content=ft.Text('Mon')),
            ft.Container(width=40, height=50, border_radius=ft.border_radius.all(80),
                         on_hover=lambda e: select_day_hover(e),
                         on_click=lambda e: select_day_click(e), alignment=ft.alignment.center, bgcolor='#ffffff',
                         content=ft.Text('Tue')),
            ft.Container(width=40, height=50, border_radius=ft.border_radius.all(80),
                         on_hover=lambda e: select_day_hover(e),
                         on_click=lambda e: select_day_click(e), alignment=ft.alignment.center, bgcolor='#ffffff',
                         content=ft.Text('Wed')),
            ft.Container(width=40, height=50, border_radius=ft.border_radius.all(80),
                         on_hover=lambda e: select_day_hover(e),
                         on_click=lambda e: select_day_click(e), alignment=ft.alignment.center, bgcolor='#ffffff',
                         content=ft.Text('Thu')),
            ft.Container(width=40, height=50, border_radius=ft.border_radius.all(80),
                         on_hover=lambda e: select_day_hover(e),
                         on_click=lambda e: select_day_click(e), alignment=ft.alignment.center, bgcolor='#ffffff',
                         content=ft.Text('Fri')),
            ft.Container(width=40, height=50, border_radius=ft.border_radius.all(80),
                         on_hover=lambda e: select_day_hover(e),
                         on_click=lambda e: select_day_click(e), alignment=ft.alignment.center, bgcolor='#ffffff',
                         content=ft.Text('Sat'))
        ])
                                   )

        return _select_day

class ControllerReminder(ft.UserControl):
    def build(self):
        def select_time(e):
            pass

        def limit_keyboard_input(e):
            print(e.control.data)
            if e.control.data in ['year-start', 'year-end']:
                value = e.control.value
                if len(value) <= 4:
                    if len(value) > 0:
                        for i in value:
                            if not i.isnumeric():
                                e.control.value = ''
                else:
                    e.control.value = ''
            else:
                value = e.control.value
                if len(value) <= 2:
                    if len(value) > 0:
                        for i in value:
                            if not i.isnumeric():
                                e.control.value = ''
                else:
                    e.control.value = ''
            e.control.update()

        _set_reminder = ft.Container(height=70, content=
        ft.Row(spacing=15, alignment=ft.MainAxisAlignment('center'), controls=[
            ft.Container(content=ft.Text('Alarm', size=22, weight="w700")),
            ft.Container(width=60, alignment=ft.alignment.center, content=ft.Switch(value=False)),
            ft.Container(height=40, border_radius=ft.border_radius.all(20), padding=ft.padding.all(0),
                         bgcolor='#ffffff', content=ft.Row(spacing=0, controls=[
                    ft.Container(bgcolor='#ffffff', border_radius=ft.border_radius.all(20),
                                 content=ft.TextField(data='hour', hint_text='12', width=40, cursor_height=20, text_size=18,
                                                      border=ft.InputBorder('none'),
                                                      on_change=lambda e: limit_keyboard_input(e),
                                                      keyboard_type=ft.KeyboardType.NUMBER,
                                                      content_padding=ft.padding.only(bottom=7, top=0, left=10))),
                    ft.Container(bgcolor='#ffffff', content=ft.Text(':', size=22)),
                    ft.Container(bgcolor='#ffffff',
                                 content=ft.TextField(data='minute', hint_text='00', width=50, cursor_height=20,
                                                      text_size=18,
                                                      border=ft.InputBorder('none'), keyboard_type=ft.KeyboardType.NUMBER,
                                                      content_padding=ft.padding.only(bottom=7, top=0, left=8))),
                    ft.Container(padding=ft.padding.only(left=5),
                                 content=ft.Dropdown(content_padding=ft.padding.only(bottom=5, top=0, left=8),
                                                     on_change=lambda e: select_time(e), border=ft.InputBorder('none'),
                                                     value='AM', label_style=ft.TextStyle(size=18), width=60, options=[
                                         ft.dropdown.Option("AM"),
                                         ft.dropdown.Option("PM"),
                                     ]))
                ]))
        ]))

        return _set_reminder

class ControllerRepeat(ft.UserControl):
    def build(self):
        def select_day_hover(e):
            if e.control.bgcolor != ft.colors.BLACK:
                if e.data == 'true':
                    e.control.bgcolor = ft.colors.BLACK12
                else:
                    e.control.bgcolor = '#ffffff'
                e.control.update()

        def select_timerange(e):
            if e.control.bgcolor in ['#ffffff', ft.colors.BLACK12]:
                # Active
                e.control.bgcolor = ft.colors.BLACK
                e.control.content.color = ft.colors.WHITE
                e.control.update()
            else:
                e.control.bgcolor = '#ffffff'
                e.control.content.color = ft.colors.BLACK
                e.control.update()

        _set_repeat = ft.Container(height=80, content=ft.Column(controls=[
            ft.Container(margin=ft.margin.only(left=30), content=ft.Text('Repeat', size=18)),
            ft.Row(spacing=0, alignment=ft.MainAxisAlignment('spaceEvenly'), controls=[
                ft.Container(width=70, height=30, border_radius=ft.border_radius.all(80),
                             on_hover=lambda e: select_day_hover(e),
                             on_click=lambda e: select_timerange(e), alignment=ft.alignment.center, bgcolor='#ffffff',
                             content=ft.Text('Daily')),
                ft.Container(width=70, height=30, border_radius=ft.border_radius.all(80),
                             on_hover=lambda e: select_day_hover(e),
                             on_click=lambda e: select_timerange(e), alignment=ft.alignment.center, bgcolor='#ffffff',
                             content=ft.Text('Weekly')),
                ft.Container(width=70, height=30, border_radius=ft.border_radius.all(80),
                             on_hover=lambda e: select_day_hover(e),
                             on_click=lambda e: select_timerange(e), alignment=ft.alignment.center, bgcolor='#ffffff',
                             content=ft.Text('Monthly')),
            ])]))

        return _set_repeat

class ControllerDateRange(ft.UserControl):
    def build(self):
        _set_daterange = ft.Container(height=90, margin=ft.margin.only(left=20), content=ft.Column(controls=[
            ft.Row(spacing=15, alignment=ft.MainAxisAlignment('start'), controls=[
                ft.Container(width=70, content=ft.Text('Start', size=20)),
                ft.Container(height=40, border_radius=ft.border_radius.all(20), padding=ft.padding.all(0),
                             bgcolor='#ffffff', content=ft.Row(spacing=0, controls=[
                        ft.Container(bgcolor='#ffffff', border_radius=ft.border_radius.all(20),
                                     content=ft.TextField(data='month', hint_text='MM', width=50, cursor_height=20,
                                                          text_size=18, keyboard_type=ft.KeyboardType.NUMBER,
                                                          on_change=lambda e: limit_keyboard_input(e),
                                                          border=ft.InputBorder('none'), hint_style=ft.TextStyle(size=14),
                                                          content_padding=ft.padding.only(bottom=7, top=0, left=10))),
                        ft.Container(bgcolor='#ffffff', content=ft.Text('/', size=22)),
                        ft.Container(bgcolor='#ffffff',
                                     content=ft.TextField(data='day', hint_text='DD', width=50, cursor_height=20,
                                                          text_size=18,
                                                          border=ft.InputBorder('none'), hint_style=ft.TextStyle(size=14),
                                                          content_padding=ft.padding.only(bottom=7, top=0, left=8))),
                        ft.Container(bgcolor='#ffffff', content=ft.Text('/', size=22)),
                        ft.Container(bgcolor='#ffffff', border_radius=ft.border_radius.all(20),
                                     content=ft.TextField(data='year-start', hint_text='YYYY', width=70, cursor_height=20,
                                                          text_size=18, on_change= lambda e: limit_keyboard_input(e),
                                                          border=ft.InputBorder('none'), hint_style=ft.TextStyle(size=14),
                                                          content_padding=ft.padding.only(bottom=7, top=0, left=8))),
                    ]))
            ]),
            ft.Row(spacing=15, alignment=ft.MainAxisAlignment('start'), controls=[
                ft.Container(width=70, content=ft.Text('End', size=20)),
                ft.Container(height=40, border_radius=ft.border_radius.all(20), padding=ft.padding.all(0),
                             bgcolor='#ffffff', content=ft.Row(spacing=0, controls=[
                        ft.Container(bgcolor='#ffffff', border_radius=ft.border_radius.all(20),
                                     content=ft.TextField(data='month', hint_text='MM', width=50, cursor_height=20,
                                                          text_size=18,
                                                          border=ft.InputBorder('none'), hint_style=ft.TextStyle(size=14),
                                                          content_padding=ft.padding.only(bottom=7, top=0, left=10))),
                        ft.Container(bgcolor='#ffffff', content=ft.Text('/', size=22)),
                        ft.Container(bgcolor='#ffffff',
                                     content=ft.TextField(data='day', hint_text='DD', width=50, cursor_height=20,
                                                          text_size=18, on_change=lambda e: limit_keyboard_input(e),
                                                          border=ft.InputBorder('none'), hint_style=ft.TextStyle(size=14),
                                                          content_padding=ft.padding.only(bottom=7, top=0, left=8))),
                        ft.Container(bgcolor='#ffffff', content=ft.Text('/', size=22)),
                        ft.Container(bgcolor='#ffffff', border_radius=ft.border_radius.all(20),
                                     content=ft.TextField(data='year-end', hint_text='YYYY', width=70, cursor_height=20,
                                                          text_size=18, on_change=lambda e: limit_keyboard_input(e),
                                                          border=ft.InputBorder('none'), hint_style=ft.TextStyle(size=14),
                                                          content_padding=ft.padding.only(bottom=7, top=0, left=8))),
                    ]))
            ])
        ]))
        return _set_daterange

class ControllerSetGoal(ft.UserControl):
    def build(self):

        def icon_hover(e):
            if e.data == 'true':
                # Active
                e.control.bgcolor = '#8bc9e1'
                e.control.update()
            else:
                e.control.bgcolor = '#cee8f2'
                e.control.update()

        _set_goal = ft.Container(height=130, alignment=ft.alignment.center, margin=ft.margin.only(top=15),
            content=ft.Column(spacing=0, width=325, horizontal_alignment=ft.CrossAxisAlignment('center'), controls=[
            ft.Container(bgcolor=ft.colors.WHITE, height=40, alignment=ft.alignment.center, content=ft.Text('Select a target', size=16)),
            ft.Container(bgcolor=ft.colors.WHITE, height=70, content=
        ft.Row(spacing=15, alignment=ft.MainAxisAlignment('center'), controls=[
            ft.Container(on_hover=lambda e: icon_hover(e), width=80, height=40, bgcolor='#cee8f2', padding=ft.padding.only(right=12), border_radius=ft.border_radius.all(35), content=ft.Row(spacing=0, controls=[
                ft.Image('/add_icon.png', expand=True, border_radius=ft.border_radius.all(100), width=25, height=25),
                ft.Text('Icon', size=14, weight='w500')
                ])),

            ft.Container(content=ft.TextField(label='Your Target', width=100, hint_style=ft.TextStyle(size=14), height=35,
                                              label_style=ft.TextStyle(size=14), border=ft.InputBorder('underline'))),
            ft.Container(height=35, border_radius=ft.border_radius.all(20), bgcolor='#ffffff',
                         content=ft.Row(spacing=0, controls=[
                             ft.Container(content=ft.Dropdown(content_padding=ft.padding.only(top=0, left=0),
                                                              on_change=lambda e: select_time(e),
                                                              border=ft.InputBorder('none'), value='min',
                                                              label_style=ft.TextStyle(size=10), width=30, options=[
                                                  ft.dropdown.Option("AM"),
                                                  ft.dropdown.Option("PM"),
                                              ]))
                         ]))
        ]))]))

        return _set_goal

class ControllerSetCommet(ft.UserControl):
    def build(self):

        _set_comment = ft.Container(height=120, alignment=ft.alignment.center, content=
            ft.Container(width=320,  bgcolor=ft.colors.CYAN_50, content=ft.TextField(label='Write a comment',
            expand=True, capitalization=ft.TextCapitalization(value='sentences'), multiline=True, min_lines=4, max_lines=4, border_radius=ft.border_radius.all(20),)))

        return _set_comment

class ControllerSubmitBtn(ft.UserControl):
    def build(self):
        _submit_btn = ft.Container(expand=True, alignment=ft.alignment.center, margin=ft.margin.only(bottom=7),
                                   content=ft.Container(width=140, height=40,
                                                        content=ft.ElevatedButton('Add Habit!', elevation=4,
                                                                                  bgcolor=ft.colors.CYAN_ACCENT_400)))

        return _submit_btn