{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {

  packages = [
    pkgs.python3
    pkgs.uv
    pkgs.nodejs_20
    pkgs.git
  ];

  shellHook = ''
    uv pip install
    source .venv/bin/activate
  '';
}
