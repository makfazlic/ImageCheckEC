# ImageCheckEC

ImageCheckEC is an internal project of the ETH Entrepreneur Club that focuses on cropping and adjusting images, including handling transparency, for various club-related purposes. This tool simplifies image manipulation tasks, making it easy to center and make logos transparent or center faces for website or presentation purposes.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Cropping and Adjusting Logos](#cropping-and-adjusting-logos)
  - [Centering Faces](#centering-faces)
  - [Processing Images from CSV](#processing-images-from-csv)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your system.
- Git installed on your system (for cloning the repository).

### Installation

1. Clone the ImageCheckEC repository to your local machine:

   ```shell
   git clone https://github.com/makfazlic/ImageCheckEC.git
   ```

2. Navigate to the project directory:

   ```shell
   cd ImageCheckEC
   ```

3. Make the Python environment for this project:

   ```shell
   python3 -m venv imagecheckec_env
   ```

4. Install the required Python packages using pip:

   ```shell
   pip install -r requirements.txt
   ```

Now, you're ready to start using ImageCheckEC!

## Usage

ImageCheckEC provides two main modes for image manipulation: `logo` and `face`. Depending on your requirements, you can use the following commands:

### Processing images from a Folder

For website or presentation purposes, you can process face images using the following command where `-f` takes as input a folder location and `-s` is size e.g. 500 to make the face images 500x500. Other ratios are not possible. If the `-s` is not included 512 is the default value.

```shell
python run.py -m face -f ./my-face-images/ -s 500
```

The outputed faces are properly centered and 500x500, while being in webp format. This makes images more suitable for websites.

### Processing Images from CSV

You can also process images from a CSV file. Use the following command, where `-c` is for a CSV file and `-i` is the index of a column that contains images, counting from 0:

```shell
python run.py -m face -c my-csv-file.csv -i 10 -s 300
```

This command will process images from the specified CSV file, centering faces in the images listed in the specified column.

## Contributing

We welcome contributions from the ETH Entrepreneur Club community! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository on GitHub.
2. Create a new branch for your feature or bug fix.
3. Make your changes and test them thoroughly.
4. Submit a pull request to the main repository's `main` branch.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
