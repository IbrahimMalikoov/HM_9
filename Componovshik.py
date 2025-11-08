from abc import ABC, abstractmethod


class FileSystemComponent(ABC):
    """Абстрактный компонент файловой системы"""

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def display(self, indent=""):
        pass

    @abstractmethod
    def get_size(self):
        pass


class File(FileSystemComponent):
    """Класс, представляющий файл (Лист)"""

    def __init__(self, name, size):
        super().__init__(name)
        self._size = size

    def display(self, indent=""):
        print(f"{indent}Файл: {self.name} ({self._size} KB)")

    def get_size(self):
        # ВАЖНО: Размер файла
        return self._size


class Directory(FileSystemComponent):
    """Класс, представляющий папку (Компоновщик)"""

    def __init__(self, name):
        super().__init__(name)
        self._children = []

    def add(self, component):
        # ВАЖНО: Проверка на наличие компонента
        if component not in self._children:
            self._children.append(component)

    def remove(self, component):
        if component in self._children:
            self._children.remove(component)

    def display(self, indent=""):
        print(f"{indent}Папка: {self.name}")
        for child in self._children:
            child.display(indent + "  ")

    def get_size(self):
        total_size = 0
        for child in self._children:
            total_size += child.get_size()
        return total_size


# Клиентский код
if __name__ == "__main__":
    # Создание файлов
    file1 = File("document.txt", 120)
    file2 = File("image.jpg", 250)
    file3 = File("archive.zip", 1024)
    file4 = File("presentation.pptx", 300)

    # Создание папок
    root = Directory("Корень")
    documents = Directory("Документы")
    pictures = Directory("Изображения")

    # Вложенная папка
    work_docs = Directory("Рабочие")

    # Формирование иерархии
    root.add(documents)
    root.add(pictures)
    root.add(file3)

    documents.add(file1)
    documents.add(work_docs)
    work_docs.add(file4)

    pictures.add(file2)

    # Попытка добавить существующий компонент
    pictures.add(file2)

    # Вывод структуры и размеров
    print("Структура файловой системы:")
    root.display()

    print("\nРазмеры:")
    print(f"Размер файла '{file1.name}': {file1.get_size()} KB")
    print(f"Размер папки '{documents.name}': {documents.get_size()} KB")
    print(f"Общий размер в корневой папке: {root.get_size()} KB")

    # Удаление компонента
    documents.remove(work_docs)
    print("\nСтруктура после удаления папки 'Рабочие':")
    root.display()
    print(f"\nНовый размер папки '{documents.name}': {documents.get_size()} KB")