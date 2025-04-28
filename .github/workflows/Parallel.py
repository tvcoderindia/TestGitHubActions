name: Parallel-Build-Workflow

permissions:
  id-token: write
  contents: write

on:
  push:

jobs:

  get-runner:
    if: ${{ always() }}
    runs-on: [windows-latest]
    outputs:
     RUNNER: ${{ runner.name }}
    steps:
      - name: Set Runner
        run: echo "selected runner = ${{ runner.name }}"

       - name: Set Environment Variable
        run: |
              $a = "abc"
              echo "$a=A_VARIABLE" >> $GITHUB_ENV
        shell: pwsh

  build:
    needs: get-runner
    runs-on: ${{needs.get-runner.outputs.RUNNER}}
    steps:
      - name: Checkout Code
        uses: actions/checkout@v4
        with:
              fetch-depth: 0
     

  Test:
    needs: get-runner
    runs-on: ${{needs.get-runner.outputs.RUNNER}}
    steps:
      - name: Checkout Code
        uses: actions/checkout@v4
        with:
              fetch-depth: 0

      - name: Get Environment Variable
        run: |
              write-host ${{ env.A_VARIABLE }}
        shell: pwsh
