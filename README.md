# DevDeck - Key Light
![CI](https://github.com/jamesridgway/devdeck-hijri/workflows/CI/badge.svg?branch=main)

Elgato Key Light controls for [DevDeck](https://github.com/jamesridgway/devdeck).

## Installing
Simplify install *DevDeck - Key Light* into the same python environment that you have installed DevDeck.

    pip install devdeck-hijri

You can then update your DevDeck configuration to use decks and controls from this package.

## Controls

* `KeylightToggleControl`

   Can be used to toggle the state of an Elgato Key Light

## Configuration

Example configuration:

    decks:
      - serial_number: ABC123
        name: devdeck.decks.single_page_deck_controller.SinglePageDeckController
        settings:
          controls:
            - name: devdeck_hijri.hijri_toggle_control.HijriToggleControl
              key: 0
              settings:
                host: 192.168.1.23
