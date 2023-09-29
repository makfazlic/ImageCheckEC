# ImageCheckEC

ImageCheckEC is an internal project of the ETH Entrepreneur Club that focuses on cropping and adjusting images, including handling transparency, for various club-related purposes. This tool simplifies image manipulation tasks, making it easy to center and make logos transparent or center faces for website or presentation purposes.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Cropping and Adjusting Logos](#cropping-and-adjusting-logos)
  - [Centering Faces](#centering-faces)
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
   git clone https://github.com/eth-entrepreneur-club/ImageCheckEC.git
   ```

2. Navigate to the project directory:

   ```shell
   cd ImageCheckEC
   ```

3. Install the required Python packages using pip:

   ```shell
   pip install -r requirements.txt
   ```

Now, you're ready to start using ImageCheckEC!

## Usage

ImageCheckEC provides two main modes for image manipulation: `logo` and `face`. Depending on your requirements, you can use the following commands:

### Cropping and Adjusting Logos

To center and make logos transparent, use the following command:

```shell
python run.py -m logo
```

This mode is useful for adjusting logos to meet the specific design requirements of the ETH Entrepreneur Club.

### Centering Faces

For website or presentation purposes, you can center faces in images using the following command:

```shell
python run.py -m face
```

This mode helps ensure that faces are properly centered, making your images more aesthetically pleasing.

## Contributing

We welcome contributions from the ETH Entrepreneur Club community! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository on GitHub.
2. Create a new branch for your feature or bug fix.
3. Make your changes and test them thoroughly.
4. Submit a pull request to the main repository's `main` branch.

For more details on contributing, please check out our [Contributing Guidelines](CONTRIBUTING.md).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

We hope that ImageCheckEC helps you with your image manipulation tasks for the ETH Entrepreneur Club. If you encounter any issues or have suggestions for improvements, please don't hesitate to [open an issue](https://github.com/eth-entrepreneur-club/ImageCheckEC/issues) on our GitHub repository.
