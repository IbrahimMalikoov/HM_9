class TV:
    """Подсистема: Телевизор"""
    def turn_on(self):
        print("Телевизор включен")

    def turn_off(self):
        print("Телевизор выключен")

    def set_channel(self, channel):
        print(f"Телевизор переключен на канал {channel}")

    def set_input(self, input_source):
        print(f"Телевизор переключен на вход {input_source}")


class AudioSystem:
    """Подсистема: Аудиосистема"""
    def turn_on(self):
        print("Аудиосистема включена")

    def turn_off(self):
        print("Аудиосистема выключена")

    def set_volume(self, level):
        # ВАЖНО: Регулировка громкости
        print(f"Громкость аудиосистемы установлена на {level}")


class DVDPlayer:
    """Подсистема: DVD-проигрыватель"""
    def play(self, movie):
        print(f"DVD-проигрыватель воспроизводит '{movie}'")

    def pause(self):
        print("DVD-проигрыватель на паузе")

    def stop(self):
        print("DVD-проигрыватель остановлен")


class GameConsole:
    """Подсистема: Игровая консоль"""
    def turn_on(self):
        print("Игровая консоль включена")

    def start_game(self, game):
        print(f"Запущена игра: {game}")


class HomeTheaterFacade:
    """Фасад для управления мультимедийной системой"""
    def __init__(self, tv, audio_system, dvd_player, game_console):
        self.tv = tv
        self.audio_system = audio_system
        self.dvd_player = dvd_player
        self.game_console = game_console

    def watch_movie(self, movie, channel, volume):
        # ВАЖНО: Сценарий просмотра фильма
        print("\nПодготовка к просмотру фильма...")
        self.tv.turn_on()
        self.tv.set_channel(channel)
        self.audio_system.turn_on()
        self.audio_system.set_volume(volume)
        self.dvd_player.play(movie)

    def end_movie(self):
        print("\nЗавершение просмотра фильма...")
        self.dvd_player.stop()
        self.audio_system.turn_off()
        self.tv.turn_off()

    def play_game(self, game, volume):
        # ВАЖНО: Сценарий запуска игры
        print("\nЗапуск игровой сессии...")
        self.tv.turn_on()
        self.tv.set_input("HDMI 2")
        self.audio_system.turn_on()
        self.set_volume(volume)
        self.game_console.turn_on()
        self.game_console.start_game(game)

    def listen_to_music(self, volume):
        print("\nВключение режима прослушивания музыки...")
        self.tv.turn_on()
        self.tv.set_input("Audio")
        self.audio_system.turn_on()
        self.audio_system.set_volume(volume)

    def set_volume(self, level):
        print(f"\nРегулировка громкости через фасад...")
        self.audio_system.set_volume(level)


# Клиентский код
if __name__ == "__main__":
    tv = TV()
    audio = AudioSystem()
    dvd = DVDPlayer()
    console = GameConsole()

    home_theater = HomeTheaterFacade(tv, audio, dvd, console)

    # Сценарий просмотра фильма
    home_theater.watch_movie("Властелин колец", 5, 25)
    home_theater.end_movie()

    # Сценарий игры
    home_theater.play_game("Cyberpunk 2077", 20)

    # Сценарий прослушивания музыки
    home_theater.listen_to_music(30)

    # Регулировка громкости
    home_theater.set_volume(15)