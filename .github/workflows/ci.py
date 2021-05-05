name: PyBand Workflow
on: [push, pull_request]

jobs:
  pyband-test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.6, 3.7, 3.8, 3.9]
    if: github.event_name == 'push' || github.event.pull_request.head.repo.full_name != 'bandprotocol/pyband'

    steps:
      - name: Code Checkout
        uses: actions/checkout@v2

      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v1
        with:
          python-version: ${{ matrix.python-version }}

      - name: Install dependencies
        working-directory: ${{env.working-directory}}
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      - name: Test with pytest
        working-directory: ${{env.working-directory}}
        run: |
          pytest
