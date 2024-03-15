from abc import ABC, abstractmethod


class FileSubject(ABC):
    """
    The subject interface declares some common operations
    for both RealFileAccess and the Proxy. This allows
    the proxy to control access to real file operations.
    """

    @abstractmethod
    def read_file(self, filename: str) -> None:
        pass


class RealFileAccess(FileSubject):
    """
    The RealFileAccess class is going to contain
    the core logic for reading files.
    """
    def read_file(self, filename: str) -> None:
        print(f"Reading file {filename}")


class ProxyFileAccess(FileSubject):
    """
    The Proxy controls access to the RealFileAccess class
    and adds logging.
    """
    def __init__(self, real_file_access: RealFileAccess) -> None:
        self._real_file_access = real_file_access

    def read_file(self, filename: str) -> None:
        if self.check_access(filename):
            self._real_file_access.read_file(filename)
            self.log_access(filename)

    def check_access(self, filename: str) -> bool:
        # Example mple condition: Only allowing access to specific files.
        print(f"Proxy: Checking access to {filename}")
        return "allowed" in filename

    def log_access(self, filename: str) -> None:
        print(f"Proxy: Logging access to {filename}")


def client_code(file_subject: FileSubject, filename: str) -> None:
    """
    This is the client code that works with file subjects via the
    FileSubject interface.
    :param file_subject:
    :param filename:
    :return:
    """
    file_subject.read_file(filename)


if __name__ == "__main__":
    real_access = RealFileAccess()
    proxy_access = ProxyFileAccess(real_access)
    print("Client: Trying to access a restricted file without proxy")
    client_code(real_access, "restricted_file.txt")
    print("Client: Trying to access an allowed file with the proxy")
    client_code(proxy_access, "allowed_file.txt")