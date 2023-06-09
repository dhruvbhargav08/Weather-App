from flet import *
import datetime
days = [
    "Mon",
    "Tue",
    "Wed",
    "Thu",
    "Fri",
    "Sat",
    "Sun",
]
def bot_data(_current):
            _botdata = []
            for index in range(1, 8):
                _botdata.append(
                    Row(
                        spacing=5,
                        alignment="spaceBetween",
                        controls=[
                            Row(
                                expand=1,
                                alignment="start",
                                controls=[
                                    Container(
                                        alignment=alignment.center,
                                        content=Text(
                                            days[
                                                datetime.datetime.weekday(
                                                    datetime.datetime.fromtimestamp(
                                                        _current.json()["daily"][index]["dt"]
                                                    )
                                                )
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                            Row(
                                expand=1,
                                controls=[
                                    Container(
                                        content=Row(
                                            alignment="start",
                                            controls=[
                                                Container(
                                                    width=20,
                                                    height=20,
                                                    alignment=alignment.center_left,
                                                    content=Image(
                                                        src=f'../assests/forecast/{_current.json()["daily"][index]["weather"][0]["main"].lower()}.png',
                                                    ),
                                                ),
                                                Text(
                                                    _current.json()["daily"][index]["weather"][0][
                                                        "main"],
                                                    size=11,
                                                    color="white54",
                                                    text_align="center",
                                                )
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                            Row(
                                expand=1,
                                alignment="end",
                                controls=[
                                    Container(
                                        alignment=alignment.center,
                                        content=Row(
                                            alignment="center",
                                            spacing=5,
                                            controls=[
                                                Container(
                                                    width=20,
                                                    content=Text(
                                                        int(_current.json()["daily"][index]["temp"][
                                                                "max"] - 273),
                                                    )
                                                )
                                            ]
                                        )
                                    )
                                ]
                            )
                        ],
                    )
                )
            return _botdata