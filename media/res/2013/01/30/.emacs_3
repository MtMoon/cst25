;; color-theme settings
;(require 'color-theme)
;(color-theme-initialize)
;(color-theme-billw)

;; ;; w3m settings
;(require 'w3m-load)
;(setq browse-url-browser-function 'w3m-goto-url)
;(autoload 'w3m-goto-url "w3m" "Ask a WWW browser to show a URL." t)
;(setq w3m-use-cookies t
;      w3m-default-display-inline-images t)
;(global-set-key "\C-c\C-w" 'w3m-goto-url)

;;  disable menu bar
(menu-bar-mode -1)

;; ;; EMMS
;; (require 'emms-setup)
;; (emms-standard)
;; ;; players
;; (setq emms-player-mpg321-command-name "mpg123"
;;       emms-player-mplayer-command-name "mplayer"
;;       emms-player-mplayer-parameters '("-slave")
;;       emms-player-list '(emms-player-mplayer
;; 			 emms-player-mplayer-playlist
;; 			 emms-player-mpg321))
;; ;; Show the current track each time EMMS starts to play a track with ">"
;; (add-hook 'emms-player-started-hook 'emms-show)
;; (setq emms-show-format "play-> %s")
;; ;; default music directory
;; (setq emms-source-file-default-directory "~/music"
;;       emms-repeat-playlist nil
;;       emms-playlist-buffer-name "music")

;; ;; shortkeys
;; (global-set-key "\C-cey" 'emms-play-directory)
;; (global-set-key "\C-cex" 'emms-play-dired)
;; (global-set-key "\C-cel" 'emms-playlist-mode-go)
;; (global-set-key "\C-ces" 'emms-start)
;; (global-set-key "\C-cee" 'emms-stop)
;; (global-set-key "\C-cen" 'emms-next)
;; (global-set-key "\C-ceb" 'emms-previous)
;; (global-set-key "\C-cep" 'emms-pause)
;; (global-set-key "\C-cea" 'emms-add-file)
;; (global-set-key "\C-ced" 'emms-add-directory)
;; (global-set-key (kbd "C-c +") 'emms-volume-mode-plus)
;; (global-set-key (kbd "C-c -") 'emms-volume-mode-minus)

;; Emacs
(show-paren-mode t)
(tool-bar-mode 0)
(scroll-bar-mode 0)
(setq inhibit-startup-screen t)
(display-time-mode t)
(display-battery-mode t)
(global-set-key (kbd "<f2>") 'eshell)

(defun my-fullscreen()
  (interactive)
  (x-send-client-message
   nil 0 nil "_NET_WM_STATE" 32
   '(2 "_NET_WM_STATE_FULLSCREEN" 0)))
(global-set-key (kbd "<f11>") 'my-fullscreen)
(global-set-key (kbd "<f10>") 'toggle-menu-bar-mode-from-frame)

;(my-fullscreen)

; backup
(setq backup-directory-alist '(("." . "~/.emacs.d/backup")))
(setq version-control t)
(setq kept-new-versions 100)

;; C language
(setq c-basic-offset 4
      c-default-style "linux")

(defun my-programming-style()
  (interactive)
  (local-set-key "\C-cc" 'compile)
  (local-set-key "\r" 'newline-and-indent)
  (auto-fill-mode 1))

;; C language
(add-hook 'c-mode-common-hook 'my-programming-style)

;; Perl language
(add-hook 'perl-mode-hook 'my-programming-style)

;; Python language
(add-hook 'python-mode-hook 'my-programming-style)

;; Auto Fill Settings
(global-set-key (kbd "<f9>") 'auto-fill-mode)

;; ;; VM - Mail
;; (add-to-list 'load-path
;; 	     (expand-file-name "~/.emacs.d/site-lisp/vm"))
;; (require 'vm-autoloads)
;; (setq vm-init-file "~/.vm.el")

;; ;; System
;; (global-set-key "\C-czs" '(lambda() (interactive)
;; 			    (shell-command "sudo pm-suspend")))
;; (global-set-key "\C-czh" '(lambda() (interactive)
;; 			    (save-some-buffers)
;; 			    (shell-command "sudo halt")))
;; (global-set-key "\C-czr" '(lambda() (interactive)
;; 			    (save-some-buffers)
;; 			    (shell-command "sudo reboot")))
;; (global-set-key "\C-czw" '(lambda() (interactive)
;; 			    (shell-command "sudo wlanup")))
;; (global-set-key "\C-czb" '(lambda() (interactive)
;; 			    (shell-command "battery")))

;;(setq dired-listing-switches "-l")
;;(require 'xcscope)

;; ;; ECB Settings
;; (require 'ecb)
;; (setq ecb-tip-of-the-day nil)
;; (setq ecb-layout-name "right1")
;; (global-set-key "\C-c\C-e\C-a" 'ecb-activate)
;; (global-set-key "\C-c\C-e\C-d" 'ecb-deactivate)

;; ;; etags
;; (setq tags-table-list '("~/src/linux"))

;; ;; Semantic Settings
;; (require 'cedet)
;; (semantic-load-enable-minimum-features)
;; (setq semanticdb-project-roots
;;       (list
;;        (expand-file-name "~/src/linux")))
;; (setq semanticdb-default-save-directory "~/.emacs.d/semantic")

;; The Shell
(eshell)

(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(custom-enabled-themes (quote (manoj-dark))))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 )
