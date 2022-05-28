# "Send Matrix Message" Github Action

This Github action send a message to a Matrix Channel

## Example workflow

````yaml
# …
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
# …
      - name: Send Matrix notification message
        id: matrix-notification
        uses: tobiasge/action-send-matrix-message@v1
        with:
            homeserver: 'https://matrix.kappa-velorum.net'
            token: ${{ secrets.MATRIX_TOKEN }}
            channel: 'Channel ID'
            message: |
                This is a message
# …        
````
