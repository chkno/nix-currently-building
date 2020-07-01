{ pkgs ? import <nixpkgs> { } }:
pkgs.python3Packages.callPackage ({ lib, buildPythonPackage, }:
  buildPythonPackage rec {
    pname = "nix-currently-building";
    version = "1.0.0";
    src = lib.cleanSource ./.;
  }) { }
