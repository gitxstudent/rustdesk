# File pate on macOS

MacOS cannot use `fuse` because of [macfuse is not supported by default](https://github.com/macfuse/macfuse/wiki/Getting-Started#enabling-support-for-third-party-kernel-extensions-apple-silicon-macs).

1. Use a temporary file `/tmp/vnfap_<uuid>` as a placeholder in the pasteboard.
2. Uses `fsevent` to observe files paste operation. Then perform pasting files.

## Files

### `pasteboard_context.rs`

The context manager of the paste operations.

### `item_data_provider.rs`

1. Set pasteboard item.
2. Create temp file in `/tmp/.vnfap_*`.

### `paste_observer.rs`

Use `fsevent` to observe the paste operation with the source file `/tmp/.vnfap_*`.

### `paste_task.rs`

Perform the paste.
