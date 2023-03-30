unit main;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, StdCtrls, Buttons,
  ComCtrls, ExtCtrls, uPSComponent, TAGraph, einstellungen;

type

  { TForm1 }

  TForm1 = class(TForm)
    btnsetup: TBitBtn;
    lbldauer: TLabel;
    lbldauer2: TLabel;
    lbluptime: TLabel;
    lblresttime: TLabel;
    update_timer: TTimer;
    procedure btnsetupClick(Sender: TObject);
    procedure FormCreate(Sender: TObject);

  private

  public

  end;

var
  Form1: TForm1;

implementation

{$R *.lfm}

{ TForm1 }


procedure TForm1.btnsetupClick(Sender: TObject);
begin
  Form2.Show;
end;

procedure TForm1.FormCreate(Sender: TObject);
var
  Lines: TStrings;
  i: integer;
begin;
      Lines := TStringList.Create;
     try
        Lines.LoadFromFile('/home/luca/Luca/Privat/Python/digitalhealth/digital_health.txt');
        lbluptime.Caption:= Lines[1];
        lblresttime.Caption:=Lines[0];
     finally
     Lines.Free;
     end;
end;

end.

