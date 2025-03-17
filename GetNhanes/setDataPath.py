# setDataPath.py
import os
from typing import Optional


class PathManager:
    """
    一个用于管理全局基础路径的单例类。
    提供设置和获取基础路径的功能，确保路径在程序运行期间一致。
    """

    def __init__(self):
        """初始化 PathManager，基础路径默认为 None"""
        self._basepath: Optional[str] = None

    def set_basepath(self, path: str) -> None:
        """
        设置基础路径。

        Args:
            path (str): 要设置为基础路径的目录或文件路径。

        Raises:
            TypeError: 如果传入的 path 不是字符串。
            ValueError: 如果路径为空或无效。
            FileNotFoundError: 如果路径不存在（可选，当前未启用）。
        """
        if not isinstance(path, str):
            raise TypeError("路径必须是字符串类型")
        if not path.strip():
            raise ValueError("路径不能为空")

        # 可选：检查路径是否存在（如果不需要可以注释掉）
        if not os.path.exists(path):
            raise FileNotFoundError(f"路径 {path} 不存在")

        # 规范化路径（处理反斜杠、前斜杠等差异）
        normalized_path = os.path.normpath(path)
        self._basepath = normalized_path

    @property
    def global_path(self) -> Optional[str]:
        """
        获取当前的基础路径。

        Returns:
            str or None: 当前设置的基础路径，如果未设置则返回 None。
        """
        return self._basepath

    def is_set(self) -> bool:
        """
        检查基础路径是否已设置。

        Returns:
            bool: 如果基础路径已设置，返回 True，否则返回 False。
        """
        return self._basepath is not None

    def join_path(self, *subpaths: str) -> str:
        """
        将子路径与基础路径拼接。

        Args:
            *subpaths (str): 一个或多个子路径。

        Returns:
            str: 拼接后的完整路径。

        Raises:
            ValueError: 如果基础路径未设置。
        """
        if not self._basepath:
            raise ValueError("基础路径未设置，请先调用 set_basepath")
        return os.path.join(self._basepath, *subpaths)

    def clear_basepath(self) -> None:
        """清除当前的基础路径，将其重置为 None"""
        self._basepath = None


# 全局单例实例
path_manager = PathManager()