#!/usr/bin/env python3
"""
Тестовый скрипт для локального запуска и проверки работы загрузки тайлов.
"""

import sys
import os

# Добавляем текущую директорию в путь для импорта
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from download_and_merge_tiles import main

if __name__ == "__main__":
    print("🚀 Запуск тестовой загрузки и объединения тайлов...")
    print("=" * 50)
    
    success = main()
    
    if success:
        print("=" * 50)
        print("✅ Тест успешно завершен!")
        print("📁 Проверьте папку 'output' для просмотра результатов")
    else:
        print("=" * 50)
        print("❌ Тест завершился с ошибкой!")
        print("📋 Проверьте логи выше для диагностики")
        
    exit(0 if success else 1)
