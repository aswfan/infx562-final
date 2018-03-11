var PageTransitions = (function () {

	var $main = $('#pt-main'),
		$pages = $main.children('div.pt-page'),
		$button1 = $('#button1'),
		$button2 = $('#button2'),
		$button3 = $('#button3'),
		$button4 = $('#button4'),
		animcursor = 1,
		pagesCount = $pages.length,
		current = 0,
		isAnimating = false,
		endCurrPage = false,
		endNextPage = false,
		animEndEventNames = {
			'WebkitAnimation': 'webkitAnimationEnd',
			'OAnimation': 'oAnimationEnd',
			'msAnimation': 'MSAnimationEnd',
			'animation': 'animationend'
		},
		// animation end event name
		animEndEventName = animEndEventNames[Modernizr.prefixed('animation')],
		// support css animations
		support = Modernizr.cssanimations;

	function init() {

		console.log($pages);

		$pages.each(function () {
			var $page = $(this);
			$page.data('originalClassList', $page.attr('class'));
		});

		$pages.eq(current).addClass('pt-page-current');

		$button1.on('click', function () {
			nextPage(1);
		});

		$button2.on('click', function () {
			nextPage(2);
		});

		$button3.on('click', function () {
			nextPage(3);
		});

		$button4.on('click', function () {
			nextPage(4);
		});

		//$iterate.on( 'click', function() {
		//	if( isAnimating ) {
		//		return false;
		//	}
		//	if( animcursor > 67 ) {
		//		animcursor = 1;
		//	}
		//	nextPage( animcursor );
		//	++animcursor;
		//} );

	}

	function nextPage(options) {
		var animation = (options.animation) ? options.animation : options;

		if (isAnimating) {
			return false;
		}

		isAnimating = true;

		var $currPage = $pages.eq(current);


		if (options == 1) {
			current = 0;
			var $nextPage = $pages.eq(0).addClass('pt-page-current'),
				outClass = '', inClass = '';
		}
		else if (options == 2) {
			current = 1;
			var $nextPage = $pages.eq(1).addClass('pt-page-current'),
				outClass = '', inClass = '';
		}
		else if (options == 3) {
			current = 2;
			var $nextPage = $pages.eq(2).addClass('pt-page-current'),
				outClass = '', inClass = '';
		}
		else if (options == 4) {
			current = 3;
			var $nextPage = $pages.eq(3).addClass('pt-page-current'),
				outClass = '', inClass = '';
		}
		/*
		if(options.showPage){
			if( options.showPage < pagesCount - 1 ) {
				current = options.showPage;
			}
			else {
				current = 0;
			}
		}
		else{
			if( current < pagesCount - 1 ) {
				++current;
			}
			else {
				current = 0;
			}
		}
		console.log("current" + current);
		console.log("next page" + options);
		
		var $nextPage = $pages.eq( current ).addClass( 'pt-page-current' ),
			outClass = '', inClass = '';
		*/

		console.log($nextPage);


		switch (animation) {

			case 1:
				outClass = 'pt-page-moveToLeft';
				inClass = 'pt-page-moveFromRight';
				break;
			case 2:
				outClass = 'pt-page-moveToRight';
				inClass = 'pt-page-moveFromLeft';
				break;
			case 3:
				outClass = 'pt-page-moveToTop';
				inClass = 'pt-page-moveFromBottom';
				break;
			case 4:
				outClass = 'pt-page-moveToBottom';
				inClass = 'pt-page-moveFromTop';
				break;
		}

		$currPage.addClass(outClass).on(animEndEventName, function () {
			$currPage.off(animEndEventName);
			endCurrPage = true;
			if (endNextPage) {
				onEndAnimation($currPage, $nextPage);
			}
		});

		$nextPage.addClass(inClass).on(animEndEventName, function () {
			$nextPage.off(animEndEventName);
			endNextPage = true;
			if (endCurrPage) {
				onEndAnimation($currPage, $nextPage);
			}
		});

		if (!support) {
			onEndAnimation($currPage, $nextPage);
		}

	}

	function onEndAnimation($outpage, $inpage) {
		endCurrPage = false;
		endNextPage = false;
		resetPage($outpage, $inpage);
		isAnimating = false;
	}

	function resetPage($outpage, $inpage) {
		$outpage.attr('class', $outpage.data('originalClassList'));
		$inpage.attr('class', $inpage.data('originalClassList') + ' pt-page-current');
	}

	init();

	return {
		init: init,
		nextPage: nextPage,
	};

})();