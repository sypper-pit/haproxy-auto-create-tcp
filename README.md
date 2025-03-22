# HAProxy Port Forward Manager

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Python Version](https://img.shields.io/badge/Python-3.6%2B-blue)
![HAProxy](https://img.shields.io/badge/HAProxy-2.0%2B-brightgreen)

## 📋 Требования
- Ubuntu/Debian сервер
- HAProxy 2.0+
- Python 3.6+
- Права sudo

---

## 🚀 Быстрый старт

### 1. Установка HAProxy
```
sudo apt update && sudo apt install haproxy
```

### 2. Настройка базовой конфигурации
вставте в файл `/etc/haproxy/haproxy.cfg` настройки из примера

### Просмотр конфигурации
```
cat /etc/haproxy/haproxy.cfg
```

## ✨ Особенности
- Валидация вводимых портов и хостов
- Автоматическая перезагрузка HAProxy
- Поддержка доменных имен и IP-адресов
- Протоколирование изменений

---

## ⚠️ Важно
- Для работы скрипта требуются права **sudo**
- Открывайте порты в брандмауэре:
  ```
  sudo ufw allow /tcp
  ```
- Для продакшн-среды:
  - Настройте HTTPS для веб-интерфейса
  - Добавьте аутентификацию
  - Регулярно делайте бэкап конфигурации

---
