# 部屋内カメラモニタリング

## 概要
本プロジェクトはRaspberry Pi 5を用いた簡易的なモニタリングシステムです。
PIRセンサーで動きを検知するとカメラモジュールにてビデオ撮影を行い、検出時間をログとして残します。
![Device.gif](docs/Device.gif)
![Captured_video.gif](docs/Captured_video.gif)

## 作成背景
私のアパートメントの部屋には、メンテナンス作業や設備点検のために人が不定期に出入りします。
そのため、誰がいつ部屋に入ったのかを記録したいと考えました。

市販のセキュリティカメラ製品は多数ありますが、動画の録画や保存には月額課金が必要なものが多く、
本プロジェクトでは、シンプルかつ無料で利用できるモニタリングシステムの作成を目的としました。

## 使用機器・言語
- Raspberry Pi 5
- Raspberry Pi Camera Module 3
- GPIO Module
- Inland SPI 1.3" 128x64 OLED V2.0 Graphic Display Module
- Inland PIR Motion Sensor Module
- Python

## 接続回路
![Circuit_diagram.png](docs/Circuit_diagram.png)

## 特徴
- PIRセンサーで動きを検知すると、カメラで10秒間の動画を録画します。
- 録画中は、LEDが点灯します。
- 検出時刻はすべてログとして記録されます。
- プログラムが終了時に、ログファイル（時刻と保存ビデオ名）を出力します。
- OLEDディスプレイは現在のシステム状態が表示されます。
  - "Motion Detected"
  - "Waiting for Motion"

## 要件

### OS packages
- libcamera-apps
- python3-picamera2
- python3-spidev

### Python packages
- openpyxl
- pillow
- gpiozero

- Python packagesは'requirements.txt'に記載されており、以下のコマンドでインストールできます。
```bash
pip install -r requirements.txt
```

## インストール
1. このレポジトリをコピーします。
2. 必要なPythonライブラリをインストールします。
3. 接続回路を参考にして、 各機器を接続します。

## 使用方法
```bash
python main.py
```

## 注記
- 本プロジェクトはRaspberry Pi OS上での動作を想定しています。
~~~~