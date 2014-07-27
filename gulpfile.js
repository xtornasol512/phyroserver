var gulp = require('gulp'),
    rename = require('gulp-rename'),
    prefix = require('gulp-autoprefixer'),
    minifycss = require('gulp-minify-css'), 
    concat = require('gulp-concat'),
    uglify = require('gulp-uglify'),
    minifyHtml = require('gulp-minify-html'); 

//  inline css inlineCss = require('gulp-inline-css')

var srcCSS = 'front-end/css/new/*.css',
    distCSS = 'front-end/dist/css',
    srcJS = 'front-end/js/codigo.js', 
    distJS = 'front-end/dist/js', 
    srcHTML = 'front-end/tpl/*.html',
    distHTML = 'front-end/dist/tpl/*.html';


gulp.task('styl', function(){
    gulp.src(srcCSS)
        .pipe(prefix(["ff > 20", "ie > 7", "Android > 2.2", "iOS > 3"], { cascade: true }))
        .pipe(gulp.dest('front-end/dist/css/'))
        .pipe(minifycss())
        .pipe(rename({suffix: '.min'}))
        .pipe(gulp.dest(distCSS));
});

gulp.task('scripts', function(){
    gulp.src(srcJS)
        .pipe(uglify())
        .pipe(concat('all.js'))
        .pipe(gulp.dest(distJS));
});

gulp.task('htmls', function(){
    gulp.src(srcHTML)
        pipe(minifyHtml())
        gulp.dest(distHTML);
});

gulp.task('watch', function(){
    gulp.watch(srcCSS, ['styl']);
    // Watch .js files
    //gulp.watch(srcJS, ['scripts']);
    //watch .html files
    //gulp.watch(srcHtml, ['htmls'])
});
gulp.task('default', function(){
    console.log('Everything will done Mr. Cxuko!');
});