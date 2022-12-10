import candidate
from PyQt5.QtWidgets import *
from view import *
from candidate import *
import csv

class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.pushButton_vote.clicked.connect(lambda: self.vote())
        self.pushButton_reset.clicked.connect(lambda: self.reset())
        self.pushButton_redguyvote.clicked.connect(lambda: self.voteforredguy())
        self.pushButton_duckvote.clicked.connect(lambda: self.voteforduck())
        self.pushButton_davidvote.clicked.connect(lambda: self.votefordavid())
        self.pushButton_submitwritein.clicked.connect(lambda: self.submit())
        self.pushButton_return.clicked.connect(lambda: self.goback())
        self.hasvoted = True
        self.votecount = 0
        self.redguy = candidate("Red guy")
        self.duck = candidate("Duck")
        self.david = candidate("David")
        self.writein = candidate("Write-in")
        self.label_candvote1.setText("Red guy")
        self.label_candvote2.setText("Duck")
        self.label_candvote3.setText("David")
        self.label_candvote4.setText("Write-in")
        self.progressBar_cand1.setValue(0)
        self.progressBar_cand2.setValue(0)
        self.progressBar_cand3.setValue(0)
        self.progressBar_cand4.setValue(0)
        self.label_votetotals.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; text-decoration: underline;\">Current Vote Totals </span><span style=\" font-size:11pt;\">(0 votes counted)</span></p></body></html>")
    def vote(self):
        try:
            x = int(self.lineEdit_voterid.text())

            with open('id.csv', 'r') as file:

                reader = csv.reader(file)
                for row in reader:
                    if x == int(row[0]):
                        self.tabWidget.setTabVisible(0, False)
                        self.tabWidget.setTabVisible(1, True)
                        self.hasvoted = False
                        self.lineEdit_voterid.setText("")
                    else:
                        self.label_invalid.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">Invalid ID!</span></p></body></html>")
            file.close()

        except ValueError:
            self.label_invalid.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">ID must be an integer!</span></p></body></html>")




    def reset(self):
        """
        Reset the election.
        """
        self.hasvoted = False
        self.votecount = 0
        self.progressBar_cand1.setValue(0)
        self.progressBar_cand2.setValue(0)
        self.progressBar_cand3.setValue(0)
        self.progressBar_cand4.setValue(0)
        self.label_invalid.setText("")
        self.label_votetotals.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; text-decoration: underline;\">Current Vote Totals </span><span style=\" font-size:11pt;\">(0 votes counted)</span></p></body></html>")
        self.duck.resetvotes()
        self.redguy.resetvotes()
        self.david.resetvotes()
        self.writein.resetvotes()

    def voteforredguy(self):
        """
        Vote for Red Guy.
        :return: Adds a vote for Red Guy.
        """
        if self.hasvoted == False:
            self.redguy.addvote()
            self.votecount += 1
            self.hasvoted = True
            self.label_votemsgredguy.setText(
                "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt;\">Vote counted for </span><span style=\" font-size:9pt; font-weight:600;\">Red Guy</span><span style=\" font-size:9pt;\">!</span></p></body></html>")
        else:
            self.label_redguyerror.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; color:#ff0000;\">You already voted! Click return to see results.</span></p></body></html>")


    def votefordavid(self):
        """
        Vote for David.
        :return: Adds a vote for David.
        """
        if self.hasvoted == False:
            self.david.addvote()
            self.votecount += 1
            self.hasvoted = True
            self.label_votemsgdavid.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:9pt;\">Vote counted for </span><span style=\" font-size:9pt; font-weight:600;\">David</span><span style=\" font-size:9pt;\">!</span></p></body></html>")
        else:
            self.label_daviderror.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; color:#ff0000;\">You already voted! Click return to see results.</span></p></body></html>")

    def voteforduck(self):
        """
        Vote for Duck.
        :return: Adds a vote for Duck.
        """
        if self.hasvoted == False:
            self.duck.addvote()
            self.votecount += 1
            self.hasvoted = True
            self.label_votemsgduck.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:9pt;\">Vote counted for </span><span style=\" font-size:9pt; font-weight:600;\">Duck</span><span style=\" font-size:9pt;\">!</span></p></body></html>")
        else:
            self.label_duckerror.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; color:#ff0000;\">You already voted! Click return to see results.</span></p></body></html>")

    def submit(self):
        """
        Submits a vote for the write-in candidate specified by the user.
        :return: Adds a vote for the write-in candidate.
        """
        x = str(self.lineEdit_writeincand.text())
        if self.hasvoted == False:
            self.writein.addvote()
            self.votecount += 1
            self.hasvoted = True
            self.label_votemsgwritein.setText(f'<html><head/><body><p align=\"center\"><span style=\" font-size:9pt;\">Vote counted for </span><span style=\" font-size:9pt; font-weight:600;\">{x}</span><span style=\" font-size:9pt;\">!</span></p></body></html>')
            self.lineEdit_writeincand.setText("")
        else:
            self.label_errorwritein.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; color:#ff0000;\">You already voted! Click return to see results.</span></p></body></html>")

    def goback(self):
        """
        Returns to the main menu.
        :return: Brings the user to the main menu.
        """
        self.label_invalid.setText("")
        self.label_votemsgredguy.setText("")
        self.label_votemsgduck.setText("")
        self.label_votemsgdavid.setText("")
        self.label_votemsgwritein.setText("")
        self.label_redguyerror.setText("")
        self.label_duckerror.setText("")
        self.label_daviderror.setText("")
        self.label_errorwritein.setText("")
        self.tabWidget.setTabVisible(0, True)
        self.tabWidget.setTabVisible(1, False)

        try:
            self.progressBar_cand1.setValue(round((self.redguy.votecount()/self.votecount)*100))
            self.progressBar_cand2.setValue(round((self.duck.votecount()/self.votecount)*100))
            self.progressBar_cand3.setValue(round((self.david.votecount()/self.votecount)*100))
            self.progressBar_cand4.setValue(round((self.writein.votecount()/self.votecount)*100))
        except:
            pass

        self.label_votetotals.setText(f'<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; text-decoration: underline;\">Current Vote Totals </span><span style=\" font-size:11pt;\">({self.votecount} votes counted)</span></p></body></html>')