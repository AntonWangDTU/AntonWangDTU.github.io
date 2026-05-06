---
layout: page
title: "Dev Environment: Arch + tmux + Neovim"
description: My personal development setup — Arch Linux as the base, tmux for session management, and Neovim as the primary editor.
img: assets/img/projects/neofetch.png
importance: 8
category: fun
related_publications: false
---

<div class="row justify-content-sm-center">
    <div class="col-sm-15 mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/arch.png" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
</div>

## Overview

This page documents my personal development environment. The goal was a minimal, keyboard-driven workflow with fast startup times and full control over every layer of the stack.

The three pillars:

- **Arch Linux** — a rolling-release distro that stays out of your way
- **tmux** — persistent terminal sessions with a clean split-pane workflow
- **Neovim** — a modal editor configured entirely in Lua

---

## Arch Linux

I chose Arch for the same reason most people do: you build it from scratch, so you understand exactly what's running. There's no default desktop environment or bundled software — just a base system you extend yourself.

### Installation Highlights


### Key Packages

| Purpose          | Package(s)                          |
| ---------------- | ----------------------------------- |
| Window manager   | `hyprland`                          |
| Terminal         | `alacritty`                             |
| Shell            | `zsh` + `starship`                  |
| AUR helper       | `yay`                               |
| Fonts            | `ttf-jetbrains-mono-nerd`           |
| Compositor       | `hyprland` (built-in)               |

---

## tmux

tmux keeps sessions alive across disconnects and lets me split the terminal without leaving the keyboard.

### Config Highlights (`~/.tmux.conf`)

```bash
# Remap prefix from C-b to C-a
unbind C-b
set -g prefix C-a
bind C-a send-prefix

# Split panes with | and -
bind | split-window -h
bind - split-window -v

# Vim-style pane navigation
bind h select-pane -L
bind j select-pane -D
bind k select-pane -U
bind l select-pane -R

# Enable mouse support
set -g mouse on

# 256-colour + true colour
set -g default-terminal "tmux-256color"
set -ag terminal-overrides ",xterm-256color:RGB"

# Start windows and panes at 1
set -g base-index 1
setw -g pane-base-index 1
```

### Typical Session Layout

```
Window 1: editor   → Neovim (full pane)
Window 2: shell    → left pane: git / right pane: tests / bottom: server
Window 3: docs     → man pages, tldr, or a scratch buffer
```

---

## Neovim

Neovim is configured in Lua using [lazy.nvim](https://github.com/folke/lazy.nvim) as the plugin manager. The config lives in `~/.config/nvim/`.

### Directory Structure

```
~/.config/nvim/
├── init.lua
└── lua/
    ├── config/
    │   ├── lazy.lua       -- plugin manager bootstrap
    │   ├── options.lua    -- editor settings
    │   ├── keymaps.lua    -- custom key bindings
    │   └── autocmds.lua   -- autocommands
    └── plugins/
        ├── lsp.lua        -- LSP + Mason
        ├── treesitter.lua -- syntax highlighting
        ├── telescope.lua  -- fuzzy finder
        ├── cmp.lua        -- completion
        └── ui.lua         -- colorscheme, statusline, etc.
```

### Core Plugins

| Plugin                  | Purpose                                 |
| ----------------------- | --------------------------------------- |
| `lazy.nvim`             | Plugin manager                          |
| `nvim-lspconfig`        | LSP client configuration                |
| `mason.nvim`            | Install LSP servers, linters, formatters |
| `nvim-treesitter`       | Syntax highlighting & text objects      |
| `telescope.nvim`        | Fuzzy file/grep/buffer finder           |
| `nvim-cmp`              | Autocompletion engine                   |
| `conform.nvim`          | Formatting on save                      |
| `catppuccin`            | Colorscheme                             |
| `lualine.nvim`          | Statusline                              |
| `oil.nvim`              | File explorer as a buffer               |

### Key Remaps

```lua
-- Space as leader
vim.g.mapleader = " "

-- Fast file navigation
vim.keymap.set("n", "<leader>ff", "<cmd>Telescope find_files<cr>")
vim.keymap.set("n", "<leader>fg", "<cmd>Telescope live_grep<cr>")
vim.keymap.set("n", "<leader>fb", "<cmd>Telescope buffers<cr>")

-- LSP actions
vim.keymap.set("n", "gd", vim.lsp.buf.definition)
vim.keymap.set("n", "K",  vim.lsp.buf.hover)
vim.keymap.set("n", "<leader>ca", vim.lsp.buf.code_action)
vim.keymap.set("n", "<leader>rn", vim.lsp.buf.rename)
```

---

## Why This Stack?

- **Speed** — cold start from power-on to a working editor in under 5 seconds
- **Reproducibility** — dotfiles in a git repo mean any machine can be set up in minutes
- **Keyboard-first** — mouse is optional; hands never leave home row for common operations
- **Transparency** — no magic. Every behaviour is either explicit config or a plugin I chose to install

--

## My dotfiles


[https://github.com/AntonWangDTU/dotfiles](dotfiles repo)
