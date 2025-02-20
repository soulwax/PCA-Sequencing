# Global25 PCA

This project is designed to visualize PCA (Principal Component Analysis) data using a web server built with the **T3 Stack**. While the core visualization functionality is yet to be implemented, the project currently includes a CSV-to-JSON conversion tool for preparing data. The web server will leverage **Next.js**, **TypeScript**, **tRPC**, **Prisma**, and **Tailwind CSS** through the T3 Stack.

---

## Features

- **CSV to JSON Conversion**: Organizes `.csv` input files into `res/csv` and converts them into `.json` files saved in `res/json`.
- **Web Server (Planned)**: A full-stack, type-safe web application for data visualization using the T3 Stack.
- **NPM Integration**: Manage Python tasks and future web server commands via `npm run` scripts.

---

## Prerequisites

- **Python 3.6 or higher**
- **Node.js 16 or higher**
- **npm** (comes with Node.js)

---

## Installation

### 1. Clone the Repository

Clone this repository to your local machine:

```sh
git clone https://github.com/soulwax/Global25_PCA.git
cd Global25_PCA
```

### 2. Install Dependencies

Run the following command to install both Python and Node.js dependencies:

```sh
npm install
```

This will:

1. Install Python dependencies listed in `requirements.txt`.
2. Install Node.js dependencies from `package.json`.

### 3. Set Up a Python Virtual Environment (Optional)

If you prefer using a virtual environment for Python:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    ```

Then reinstall dependencies within the virtual environment:

```sh
pip install -r requirements.txt
```

---

## Folder Structure

```plaintext
Global25_PCA/
├── res/
│   ├── csv/                # Input CSV files go here.
│   ├── json/               # Output JSON files will be saved here.
├── scripts/
│   └── convert.py          # The script for converting CSV to JSON.
├── src/
│   └── app.ts              # Placeholder TypeScript entry point for T3 Stack.
├── requirements.txt        # Python dependencies.
├── package.json            # NPM configuration file.
└── README.md               # Project documentation.
```

---

## Usage

### CSV to JSON Conversion

1. Place your `.csv` files into the `res/csv/` directory.
2. Run the conversion script using the following command:

    ```sh
    npm run convert
    ```

3. The converted `.json` files will be saved in the `res/json/` directory.

   #### Example Input (`res/csv/example.csv`)

    ```csv
    ,PC1,PC2,PC3
    Example_BA_IA,-0.0156332,0.0270818,-0.0087572
    ```

   #### Example Output (`res/json/example.json`)

    ```json
    {
        "Albania_BA_IA": {
            "PC1": 0.1231566,
            "PC2": 0.1523294,
            "PC3": 0.0274544
        },
        "Example_BA_IA": {
            "PC1": -0.0156332,
            "PC2": 0.0270818,
            "PC3": -0.0087572
        }
    }
    ```

---

## Planned Web Server Development

The project will use the **T3 Stack** for building a full-stack web application to visualize PCA data.

### What is the T3 Stack?

The T3 Stack is a modern web development stack focused on simplicity, modularity, and full-stack type safety. It includes:

- **Next.js**: React framework for server-side rendering and static site generation.
- **TypeScript**: Type-safe programming language.
- **Tailwind CSS**: Utility-first CSS framework.
- **tRPC**: End-to-end typesafe APIs.
- **Prisma**: ORM for database management.

### Setting Up the T3 App (Planned)

Once implemented, you can scaffold the T3 app by running:

```sh
npm create t3-app@latest
```

The app will include features such as user authentication, database integration with Prisma, and interactive visualizations of PCA data.

---

## NPM Scripts

The following scripts are available via `npm run`:

| Script       | Description                                                                 |
|--------------|-----------------------------------------------------------------------------|
| `convert`    | Converts all `.csv` files in `res/csv` to `.json` files in `res/json`.      |
| `annotate`   | Annotates Python code with type hints using `pyannotate`.                  |
| `tree`       | Prints Python code structure as a tree using `pytreeprint`.                |

---

## Contributing

Contributions are welcome! Please submit issues or pull requests on [GitHub](https://github.com/soulwax/Global25_PCA).

---

## License

This project is licensed under the [GPL-3.0-only](https://opensource.org/licenses/GPL-3.0) license.
