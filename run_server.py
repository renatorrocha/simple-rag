#!/usr/bin/env python3
import sys
from pathlib import Path
from server import app
import uvicorn

src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))


def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
