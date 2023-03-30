unit einstellungen;

{$mode ObjFPC}{$H+}

interface

uses
  Classes, SysUtils, process, Forms, Controls, Graphics, Dialogs, StdCtrls,
  ExtCtrls, Buttons, Spin;

type

  { TForm2 }

  TForm2 = class(TForm)
    btnanwenden: TButton;
    edth: TEdit;
    edtmin: TEdit;
    edtsec: TEdit;
    Label1: TLabel;
    Label2: TLabel;
    Label3: TLabel;
    lblnutzung: TLabel;
    SpinEdit1: TSpinEdit;
    procedure btnanwendenClick(Sender: TObject);
  private

  public

  end;

var
  Form2: TForm2;

implementation

{$R *.lfm}

{ TForm2 }

procedure TForm2.btnanwendenClick(Sender: TObject);
var
   nutzungsdauer: string;
   F: TextFile;
begin
  nutzungsdauer := edth.Text+edtmin.Text+edtsec.Text;
  AssignFile(F, '/home/luca/Luca/Privat/Python/digitalhealth/digital_health.txt');
  try
    Rewrite(F);
    Write(F, nutzungsdauer, '\n');
  finally
     CloseFile(F);
  end;
end;

end.

